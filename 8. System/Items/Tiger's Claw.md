---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Concealable]]", "[[Concussive]]", "[[Fatal d10]]", "[[Illusion]]", "[[Primal]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 striking fearsome dueling pistol* is made from fine tigerwood, with the head of a tiger as the muzzle. Beneath the tiger head is a claw shaped bayonet. One of a set of four guns crafted as a gift to a Zenj family for delivery of rare healing and disease- abating herbs during an outbreak of a deadly disease in the Grand Duchy of Alkenstar, these firearms are now passed down to those who have done brave acts in service to the Zenj people. The flintlock sparks thrown by this weapon take the shape of pouncing tigers and the firearm's report sounds like a tiger's growl. Clever wielders use the firearm's report to panic their prey into mistakes and then pounce for the kill.

This firearm's bullets deal slashing damage instead of piercing and add an additional 1d6 bleed on a critical hit. This persistent bleed damage causes tiger-claw-shaped wounds to appear on the target.

**Activate—Tiger Shot** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You capitalize on the fears your firearm engenders, terrifying your foes. Make a ranged Strike with this firearm against a target. If you successfully deal damage to your target, the target is also affected by a 4th-rank [[Vision of Death]] with a spell DC of 28(DC 28 [[Will]] save). While vision of death typically takes the shape of the target's worst fear, this effect always appears to the target in the form of a majestic and ferocious tiger.

**Source:** `= this.source` (`= this.source-type`)
