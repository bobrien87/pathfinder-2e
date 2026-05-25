---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Used by theater troupes in combination with a fake blood pack, this bit of minor magic can simulate a dramatic and sudden wound. A *blood pack squib* is a small unassuming stone that is keyed to a single fake blood pack in a process that takes 1 minute.

**Activate—Burst Pack** `pf2:1` (manipulate)

**Requirements** The blood pack squib must be within 20 feet of its associated fake blood pack

**Effect** You lightly squeeze the stone and the fake blood pack dramatically bursts. The creature wearing the fake blood pack gains the benefits of a punctured fake blood pack. A single creature adjacent to the creature wearing the fake blood pack must succeed at a DC 16 [[Reflex]] save or be splattered with the fake blood, becoming [[Dazzled]] until the end of their next turn. You can also activate the blood pack squib as a reaction when the fake blood pack is punctured normally.

**Source:** `= this.source` (`= this.source-type`)
