---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Force]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

A *spiritual warhorn* is a trumpet made of horn, leather, and metal. When you play a single, long note from the warhorn, it calls forth a number of Medium spiritual manifestations of warriors to aid you, according to the horn's type. Each warrior appears in an open square adjacent to an enemy within 60 feet of you, makes a Strike for 2d6 force (with an attack bonus determined by the warhorn's type), and then disappears. The warriors can flank with one another and with you and your allies. Once the magic is used, the warhorn remains as a non-magical musical instrument.

Two warriors manifest with a +11 attack modifier.

**Source:** `= this.source` (`= this.source-type`)
