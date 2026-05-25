---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Disarm]]", "[[Finesse]]", "[[Magical]]", "[[Nonlethal]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 360}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large tree branch is alive, despite having been harvested from the sugi tree it once belonged to. This long, flexible, and limber branch is a *+1 striking whip*. When used to Strike, the branch snaps with the sound of a cracking whip but fills the air surrounding the point of impact with the pleasant scent of freshly cut cedar and a sprinkling of fallen leaves on the ground.

**Activate—A Multitude of Branches** `pf2:3` (concentrate, manipulate)

**Frequency** once per day

**Effect** You place the *branch of the great sugi* on the corpse of an unholy creature, then cause the branch to suddenly grow into a sugi tree, up to 25 feet tall with a 2-foot-wide trunk. As it grows, it emits a pulse of soothing energy, restoring 3d8+8 Hit Points to all creatures in a @Template[type:burst|distance:10]. A character can Climb the tree with a successful DC 10 [[Athletics]] check, and its branches effortlessly support the weight of any Medium or smaller creature. The sugi tree reverts to its whip form after 1 hour unless you transform it back before then.

**Activate—A Single Branch** `pf2:1` (manipulate)

You transform the *branch of the great sugi* from its tree form back into its whip form.

**Source:** `= this.source` (`= this.source-type`)
