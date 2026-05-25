---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Incapacitation]]"]
price: "{'gp': 45}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Gearbinder oil comes in a sealed pump that can squirt the oil a short distance. The oil is designed to flow through complex mechanisms and, agitated through mechanical action, foam up and form a paste that binds the works. The oil is effective against articulated constructs and machinery, including many constructs, clockworks, and mechanical hazards. You apply the oil to the target you want to bind, which must be within 10 feet of you. After the oil is applied, at the end of any round during which the target took an action with the attack, manipulate, or move trait, it must attempt a DC 20 [[Fortitude]] save. A mechanism that's [[Slowed]] 2 or more by gearbinder oil also can't use reactions. Gearbinder oil functions for up to 6 rounds before becoming an inert, oily residue.
- **Critical Success** The oil becomes inert, and the effect ends.
- **Success** The target reduces its slowed condition by 1. If the slowed condition's value is 0, the effect ends.
- **Failure** The target increases its slowed condition by 1, to a maximum of [[Slowed]] 3.
- **Critical Failure** The target increases its slowed condition by 2, to a maximum of slowed 3.

**Source:** `= this.source` (`= this.source-type`)
