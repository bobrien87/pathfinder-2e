---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're holding or wearing a [[Thieves' Toolkit]].

Opening a lock without a key is very similar to [[Disabling a Device]], but the DC of the check is determined by the complexity and construction of the lock you are attempting to pick. Locks of higher quality might require multiple successes to unlock. If you lack the proper tools, the GM might let you use improvised picks, which are treated as a shoddy toolkit.
- **Critical Success** You unlock the lock, or you achieve two successes toward opening a lock that requires more than one success. You leave no trace of your tampering.
- **Success** You open the lock, or you achieve one success toward opening a lock that requires more than one success. You leave behind damage that indicates the lock was picked on close scrutiny.
- **Critical Failure** You break your toolkit and leave behind obvious damage. Fixing a broken toolkit requires using Crafting to [[Repair]] it or else swapping in replacement picks (costing 3 sp, or 3 gp for an infiltrator thieves' toolkit).

**Source:** `= this.source` (`= this.source-type`)
