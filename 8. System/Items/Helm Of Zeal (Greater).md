---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Divine]]", "[[Focused]]", "[[Invested]]"]
price: "{'gp': 21000}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elaborate helmet is emblazoned with the divine symbols of a deity chosen when the helmet was crafted. You gain a +3 item bonus to that deity's Divine Skill.

**Activate—Rally to the Cause** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can spend only to cast a devotion spell. If you don't spend this Focus Point by the end of this turn, it's lost.

**Activate—Divine Fervor** `pf2:f` (concentrate)

**Frequency** once per hour

**Trigger** You've just used your champion's reaction

**Effect** You gain an additional reaction you can use only for your champion's reaction. You lose this reaction if you don't use it by the start of your next turn.

**Craft Requirements** You're a champion of the deity represented by the helmet.

**Source:** `= this.source` (`= this.source-type`)
