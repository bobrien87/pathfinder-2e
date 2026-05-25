---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Magical]]"]
price: "{'gp': 35}"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A glamorous buckler (Hardness 3, HP 6, BT 3) is lavishly decorated with gilding and inset gemstones that glitter in the light. While you have it raised, the glamorous buckler grants you a +1 item bonus to Deception checks to Feint.

**Activate—Dazzling Feint** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** You Feint

**Requirements** You have the glamorous buckler raised

**Effect** As you Feint, the glamorous buckler sparkles mightily. On a successful Feint, the target is [[Dazzled]] for 1 round.

HardnessHPBT363

**Source:** `= this.source` (`= this.source-type`)
