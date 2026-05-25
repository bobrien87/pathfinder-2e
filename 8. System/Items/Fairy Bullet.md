---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Fey]]", "[[Magical]]"]
price: "{'gp': 65}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:2` (concentrate)

These bullets glimmer with emerald green light that dances across the surface of the bullet like a mischievous sprite. On a successful Strike, a *fairy bullet* casts [[Revealing Light]] (DC 23 [[Reflex]] save{DC 23}) extending outward from a corner of the target's space. You choose which corner of the target's space you want the burst to extend out from at the time you declare the associated Strike. Since the *fairy bullet* is fired before *revealing light* can reveal the target, the effects don't affect the flat check for the attack roll with the *fairy bullet* if the target is [[Hidden]] from you.

**Source:** `= this.source` (`= this.source-type`)
