---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Auditory]]", "[[Invested]]", "[[Magical]]", "[[Void]]"]
price: "{'gp': 35000}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ice-blue half-mask is adorned with a wicked silver grin that covers the wearer's mouth, leaving the rest of the face uncovered. You gain a +3 item bonus to Intimidation checks.

**Activate—Hideous Wail** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The mask casts a 9th-rank [[Wails of the Damned]]

Each living creature in a @Template[emanation|distance:40] takes @Damage[8d10[void]|options:area-damage] damage and must attempt a DC 41 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes full damage.
- **Failure** The creature takes full damage and is [[Drained]] `r 1d4`.
- **Critical Failure** The creature takes double damage and is [[Drained]] 4.

**Source:** `= this.source` (`= this.source-type`)
