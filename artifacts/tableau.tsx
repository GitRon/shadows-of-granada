const players = [
  {
    name: "Kastilien", color: "#b5451b",
    desc: "Militärische Vormacht",
    slots: [{ label: "S1", fixed: "⚔️" }, { label: "S2", fixed: "⚔️" }, { label: "S3", fixed: "🌾" }]
  },
  {
    name: "Aragón", color: "#d4a017",
    desc: "Diplomatie & Handel",
    slots: [{ label: "S1", fixed: "👑" }, { label: "S2", fixed: "💰" }, { label: "S3", fixed: "👑" }]
  },
  {
    name: "Portugal", color: "#2e6b3e",
    desc: "Küstenmacht & Burgen",
    slots: [{ label: "S1", fixed: "🏰" }, { label: "S2", fixed: "⚔️" }, { label: "S3", fixed: "🏰" }]
  },
  {
    name: "Navarra", color: "#3a5a8a",
    desc: "Kirche & Pyrenäen",
    slots: [{ label: "S1", fixed: "✝️" }, { label: "S2", fixed: "✝️" }, { label: "S3", fixed: "👑" }]
  },
];

const regions = [
  { name: "Kantabrien / Pyrenäen", sub: "Startgebiet", color: "#4a7c59", w6: "–", crisis: false },
  { name: "Meseta Norte", sub: "Kalifat von Córdoba", color: "#7a9e4e", w6: "1", crisis: true },
  { name: "Toledo / Tajo", sub: "Taifa von Toledo", color: "#c8a84b", w6: "2", crisis: true },
  { name: "Valencia / Levante", sub: "Taifa von Valencia", color: "#c47a3a", w6: "3", crisis: true },
  { name: "Extremadura", sub: "Almoravidenreich", color: "#b05030", w6: "4", crisis: true },
  { name: "Andalusien / Granada", sub: "Nasridensultanat + Belagerung", color: "#a33a2e", w6: "5", crisis: true, double: true },
];

function PlayerCard({ p }) {
  return (
    <div style={{
      background: "white", border: `3px solid ${p.color}`,
      borderRadius: 10, padding: 8,
      boxShadow: "2px 2px 8px rgba(0,0,0,0.15)", flex: "1 1 160px", minWidth: 150
    }}>
      <div style={{ fontWeight: "bold", color: p.color, fontSize: 13, textAlign: "center" }}>{p.name}</div>
      <div style={{ fontSize: 9, color: "#9a7a5a", textAlign: "center", marginBottom: 8, fontStyle: "italic" }}>{p.desc}</div>
      <div style={{ display: "flex", gap: 6, justifyContent: "center" }}>
        {p.slots.map((s, si) => (
          <div key={si} style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
            <div style={{ fontSize: 8, color: "#9a7a5a", fontWeight: "bold", marginBottom: 3 }}>{s.label}</div>
            <div style={{ position: "relative", width: 52, height: 120 }}>
              {[2, 1, 0].map(ci => (
                <div key={ci} style={{
                  position: "absolute", top: ci * 20, left: 0,
                  width: 52, height: 76,
                  borderRadius: 5,
                  border: `2px dashed ${p.color}`,
                  background: ci === 0 ? "#f5f0e8" : "#faf7f2",
                  boxShadow: ci === 0 ? "1px 2px 4px rgba(0,0,0,0.12)" : "none",
                  overflow: "hidden",
                  zIndex: 3 - ci,
                }}>
                  {ci === 0 && (
                    <>
                      <div style={{ background: `${p.color}22`, padding: "2px 5px", borderBottom: `1px solid ${p.color}33` }}>
                        <div style={{ fontSize: 7, color: p.color, fontWeight: "bold" }}>Aktion</div>
                      </div>
                      <div style={{ padding: "2px 5px" }}>
                        <div style={{ fontSize: 7, color: "#9a7a5a" }}>Verst.</div>
                        <div style={{ fontSize: 11 }}>–</div>
                      </div>
                    </>
                  )}
                  {ci === 2 && (
                    <div style={{
                      position: "absolute", bottom: 3, left: 0, right: 0,
                      display: "flex", flexDirection: "column", alignItems: "center"
                    }}>
                      <div style={{ fontSize: 6, color: p.color, textTransform: "uppercase" }}>fix</div>
                      <div style={{ fontSize: 16 }}>{s.fixed}</div>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default function Tableau() {
  const [view, setView] = React.useState("kingdoms");

  return (
    <div style={{ fontFamily: "Georgia, serif", background: "#f5f0e8", minHeight: "100vh", padding: 16 }}>
      <h2 style={{ textAlign: "center", color: "#3b2a1a", marginBottom: 4, fontSize: 18 }}>RECONQUISTA – Tableaus</h2>

      <div style={{ display: "flex", gap: 8, justifyContent: "center", marginBottom: 16 }}>
        {[["kingdoms", "👑 Königreiche"], ["main", "🗺 Tableau"]].map(([key, label]) => (
          <button key={key} onClick={() => setView(key)} style={{
            padding: "5px 14px", borderRadius: 20, border: "2px solid",
            borderColor: view === key ? "#3b2a1a" : "#c0a880",
            background: view === key ? "#3b2a1a" : "white",
            color: view === key ? "white" : "#3b2a1a",
            cursor: "pointer", fontSize: 12, fontFamily: "Georgia, serif"
          }}>{label}</button>
        ))}
      </div>

      {view === "kingdoms" && (
        <>
          <p style={{ textAlign: "center", color: "#7a5c3a", fontSize: 10, marginBottom: 14 }}>
            Aufgedrucktes Symbol = permanente Startverstärkung · Kann nie abgeworfen werden
          </p>
          <div style={{ display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>
            {players.map((p, i) => <PlayerCard key={i} p={p} />)}
          </div>
        </>
      )}

      {view === "main" && (
        <>
          <p style={{ textAlign: "center", color: "#7a5c3a", fontSize: 10, marginBottom: 14 }}>
            Nord → Süd · W6 bestimmt Krisenregion · 6 = Krise ignoriert
          </p>
          <div style={{ overflowX: "auto" }}>
            <table style={{ borderCollapse: "separate", borderSpacing: 4, margin: "0 auto" }}>
              <thead>
                <tr>
                  <th style={{ fontSize: 10, color: "#7a5c3a", fontWeight: "bold", padding: "0 4px 6px", textAlign: "left" }}>REGION</th>
                  <th style={{ fontSize: 10, color: "#7a5c3a", padding: "0 4px 6px", textAlign: "center" }}>⚔️<br/>Militär</th>
                  <th style={{ fontSize: 10, color: "#7a5c3a", padding: "0 4px 6px", textAlign: "center" }}>🏘️<br/>Besiedlung</th>
                  <th style={{ fontSize: 10, color: "#7a5c3a", padding: "0 4px 6px", textAlign: "center" }}>⚠️<br/>Krise</th>
                  <th style={{ fontSize: 10, color: "#7a5c3a", padding: "0 4px 6px", textAlign: "center" }}>W6</th>
                </tr>
              </thead>
              <tbody>
                {regions.map((r, i) => (
                  <tr key={i}>
                    <td style={{ padding: "3px 0" }}>
                      <div style={{
                        background: r.color, color: "white", borderRadius: 7,
                        padding: "6px 10px", minWidth: 170,
                        boxShadow: "1px 1px 4px rgba(0,0,0,0.2)"
                      }}>
                        <div style={{ fontWeight: "bold", fontSize: 11 }}>{r.name}</div>
                        <div style={{ fontSize: 9, opacity: 0.85 }}>{r.sub}</div>
                      </div>
                    </td>
                    {["mil", "bes"].map(slot => (
                      <td key={slot} style={{ padding: "3px 4px" }}>
                        <div style={{
                          width: 64, height: 44, borderRadius: 6,
                          border: `2px dashed #b09070`,
                          background: i === 0 ? "#e8f5e9" : "#ede8de",
                          display: "flex", alignItems: "center", justifyContent: "center",
                          fontSize: 10, color: "#9a7a5a"
                        }}>
                          {i === 0 ? <span style={{ opacity: 0.5 }}>frei</span> : <span style={{ opacity: 0.3 }}>–</span>}
                        </div>
                      </td>
                    ))}
                    <td style={{ padding: "3px 4px" }}>
                      <div style={{
                        width: 64, height: 44, borderRadius: 6,
                        border: `2px dashed ${r.crisis ? "#c0392b" : "#b09070"}`,
                        background: r.crisis ? "#fdecea" : "#e8f5e9",
                        display: "flex", alignItems: "center", justifyContent: "center",
                        fontSize: r.crisis ? 18 : 10, color: r.crisis ? "#c0392b" : "#9a7a5a"
                      }}>
                        {r.double ? "🔒🔒" : r.crisis ? "🔒" : <span style={{ opacity: 0.5, fontSize: 9 }}>frei</span>}
                      </div>
                    </td>
                    <td style={{ padding: "3px 4px", textAlign: "center" }}>
                      <div style={{
                        width: 32, height: 44, borderRadius: 6,
                        border: "2px solid #b09070",
                        background: i === 0 ? "#e8f5e9" : "#ede8de",
                        display: "flex", alignItems: "center", justifyContent: "center",
                        fontSize: 14, fontWeight: "bold", color: i === 0 ? "#aaa" : "#3b2a1a"
                      }}>
                        {r.w6}
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p style={{ textAlign: "center", fontSize: 10, color: "#9a7a5a", marginTop: 10 }}>
            🔒 = fixe Regionskrise · 🔒🔒 = Granada (zwei Schichten) · W6 = 6 ignoriert Krise
          </p>
        </>
      )}
    </div>
  );
}
