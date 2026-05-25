---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Focused]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This humble sash can be worn around the waist or across the chest. A sash of prowess often bears a coloration or a pattern that represents the monastery in which you trained but can also sport religious symbology, such as the open hand of Irori. You gain a +2 item bonus to Acrobatics and Athletics skill checks.

**Activate—Effortless Mastery** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** You succeed at an Acrobatics or Athletics skill check

**Effect** You critically succeed instead.

**Activate—Reserves of Inner Strength** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can spend only to cast a qi spell. If you don't spend this Focus Point by the end of this turn, it's lost.

**Craft Requirements** You're a monk who can cast qi spells.

**Source:** `= this.source` (`= this.source-type`)
