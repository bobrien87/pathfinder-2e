---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *staff of the tempest* is usually crafted from the wood of a tree struck by lightning. It's often gnarled and blackened with the occasional spark of electricity flashing from its length. While wielding the staff, your vision is less inhibited by stormy weather. While you hold the staff, you ignore the [[Concealed]] condition from mist, precipitation, and the like.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Electric Arc]]
- **1st** [[Hydraulic Push]], [[Thunderstrike]]
- **2nd** [[Mist]], [[Resist Energy]] (electricity only), [[Thunderstrike]]
- **3rd** [[Lightning Bolt]], [[Wall of Wind]]
- **4th** [[Hydraulic Torrent]], [[Lightning Bolt]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
