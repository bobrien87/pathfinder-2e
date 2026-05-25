---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Censer]]", "[[Fire]]", "[[Magical]]", "[[Revelation]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The body of this censer is made of transparent crystal banded with dark iron. This globe hangs from a sturdy chain attached to a simple steel rod with a smooth grip.

**Activate—Light Incense** `pf2:2` (aura, manipulate)

**Frequency** once per day

**Cost** incense worth at least 5 gp

**Effect** As you light the incense, barely visible smoke issues from the censer in a hazy @Template[emanation|distance:20]. Creatures that are in the haze or later enter it are wreathed in wisps of smoke; these wisps last while the creature is in the smoke's aura and until the start of its next turn if it leaves the haze. An ally in the aura is [[Concealed]] and gains a +2 status bonus to Stealth checks. Any enemy in the aura that is or becomes [[Invisible]] appears as a translucent shape to you and your allies—it's no longer [[Hidden]], but it remains concealed.

**Source:** `= this.source` (`= this.source-type`)
