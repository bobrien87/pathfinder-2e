---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Primal]]"]
price: "{'gp': 2000}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This cloak appears to be woven from a thousand living leaves, hungry for flesh and eager to defend the cloak's wearer.

**Activate—Bite Back** `pf2:r` (concentrate)

**Frequency** once per round

**Trigger** You are damaged by a melee attack from an adjacent creature

**Effect** The leaves lash out at your attacker, rising up to reveal snapping jaws made of wicked thorns. The triggering creature must attempt a DC 30 [[Reflex]] save saving throw.
- **Success** The creature is unaffected.
- **Failure** The creature takes 2d6 piercing damage.
- **Critical Failure** The creature takes @Damage[4d6[piercing],3[bleed]] damage.

**Source:** `= this.source` (`= this.source-type`)
