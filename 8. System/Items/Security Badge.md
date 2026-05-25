---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "worn"
bulk: "—"
source: "Pathfinder #215: To Blot Out the Sun"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When displayed prominently, this iron badge grants you authority and gravitas. You gain a +1 item bonus to Intimidation checks.

**Activate—Authoritative Command** `pf2:1` (auditory, concentrate, incapacitation, linguistic, mental)

**Frequency** once per day

**Effect** You shout at a foe within 60 feet, compelling them to stand in place and drop everything they're holding. The target attempts a DC 23 [[Will]] save with the following results.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Slowed]] 1 as it does one of the following at the beginning of its next turn: stand in place or release what it's holding.
- **Failure** The target is [[Slowed]] 2 as it stands in place and releases what it's holding at the beginning of its next turn.
- **Critical Failure** The target is [[Slowed]] 3 as it spends its next turn to stand in place, release what it's holding, and place its hands in the air.

**Source:** `= this.source` (`= this.source-type`)
