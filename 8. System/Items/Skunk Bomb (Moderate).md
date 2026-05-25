---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Olfactory]]", "[[Poison]]", "[[Splash]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

Skunk bombs are made from the concentrated odors of xulgaths, hezrous, and other creatures with natural or supernatural stench. The bomb grants a +1 item bonus to attack rolls and deals 2d4 poison damage and 2 poison splash damage. Any creature hit by the bomb or in its splash area must attempt a DC 17 [[Fortitude]] save saving throw. Creatures in the splash area treat the results of their saving throw as one step better.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Sickened]] 1.
- **Failure** The target is sickened 1 and [[Slowed]] 1 while sickened.
- **Critical Failure** The target is [[Blinded]] for 1 round, [[Sickened]] 2, and slowed 1 while sickened.

Creatures sickened by the bomb emit an odor that lasts 10 minutes after the sickened condition ends (or 1 hour if they were also blinded). The odor can be removed or neutralized by using prestidigitation or similar magic or by spending 10 minutes scrubbing with ample soap and water. While the odor lasts, creatures within 30 feet can smell the target, enabling even those with a weak sense of smell to detect its presence, and all creatures gain a +1 item bonus to [[Track]] the affected creature for as long as it has the odor. A creature that has imprecise or precise scent doubles the range at which it can detect the target using this scent.

**Source:** `= this.source` (`= this.source-type`)
