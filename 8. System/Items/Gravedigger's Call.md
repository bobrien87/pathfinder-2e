---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Deadly d8]]", "[[Forceful]]", "[[Magical]]", "[[Occult]]", "[[Reach]]"]
price: "{'gp': 1700}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rusted shovel functions as a *+2 striking decaying glaive* when wielded as a weapon, but it more closely resembles a neglected tool. Its haft was carved from the trunk of a long-dead tree that once grew among the broken stones of an abandoned cemetery, and its blade was forged from shattered remnants of the armor that failed to protect those buried there. When you carry or wield a *gravedigger's call*, you gain a +1 item bonus to Perception checks to `act seek options=gravediggers-call` haunts and to skill checks to determine the reasons for a haunt or spirit's existence.

**Activate—Call the Fallen** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You cast [[Rouse Skeletons]] as a 5th-rank occult spell. The DC is 30.

**Craft Requirements** Supply one casting of *rouse skeletons* (5th rank).

**Source:** `= this.source` (`= this.source-type`)
