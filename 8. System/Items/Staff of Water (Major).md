---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *staff of water* is most often made of driftwood, sometimes lacquered blue. Carved versions often have a wave pattern. The staff smells of rain or brine. While wielding a *staff of water*, you have resistance 10 to fire.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Spout]]
- **1st** [[Create Water]], [[Hydraulic Push]]
- **2nd** [[Mist]], [[Water Walk]]
- **3rd** [[Aqueous Orb]], [[Wall of Water]]
- **4th** [[Crashing Wave]], [[Hydraulic Torrent]]
- **5th** [[Control Water]], [[Geyser]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
