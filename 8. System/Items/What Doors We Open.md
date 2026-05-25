---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*What Doors We Open* is the culmination of Aravashnial's research. Before he was captured, he performed a 1-minute ritual to erase his spells from this book and then hid it at his campsite to prevent his demonic foes from learning too many of his secrets. A spellcaster can transfer their own spells to this grimoire using a similar 1-minute ritual. When a spellcaster prepares their spells from it, they gain the ability to Activate the grimoire until their next daily preparations and gain a +2 item bonus to checks made to [[Recall Knowledge]] about demons. A grimoire's benefits apply only to spells cast via spell slots. No one can use more than one grimoire per day, nor can a grimoire be used by more than one person per day.

**Activate—Cast Out** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** If the next activity you take this round is to cast banishment prepared from this grimoire, it counts as the extra cost of adding an object that is anathema to the creature and gives the creature a –2 circumstance penalty to its save. If the targeted creature is a demon, increase this to a –3 circumstance penalty.

**Activate—Open the Door Within** `pf2:1` (manipulate)

The inside back cover of *What Doors We Open* features a realistic depiction of a bejeweled door set in a stone wall. When you Open the Door Within, you open that door to reveal an extradimensional space that otherwise functions identically to a [[Spacious Pouch (Type II)]].

**Source:** `= this.source` (`= this.source-type`)
