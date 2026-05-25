---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 6500}"
bulk: "1"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater resilient leather armor* was made from the flayed hide of an Elysian pegasus, then dyed a bright crimson so that it appears slick with fresh blood. The wearer of *assassin's skin* gains a +3 item bonus to [[Escape]] checks.

**Activate—Blood Revitalization** `pf2:f` (concentrate)

**Frequency** once per hour

**Trigger** You would take persistent bleed damage

**Effect** You don't take the persistent bleed damage and instead regain Hit Points equal to the bleed damage. The persistent bleed damage ends.

**Source:** `= this.source` (`= this.source-type`)
