---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Backswing]]", "[[Disarm]]", "[[Magical]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 450}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The weights of this *+1 striking meteor hammer* are shaped like snake heads, and anaconda scales adorn the chain.

**Activate—Coiling Chain** `pf2:1` (concentrate)

**Requirements** Your last action was a successful melee Strike or [[Trip]] with the *constricting meteor*

**Effect** The chain of the meteor hammer wraps around the target and squeezes. Attempt an Athletics check to [[Grapple]] the creature with a +1 item bonus. In addition to being [[Grabbed]] on a success, the target takes @Damage[(1d10+7)[bludgeoning]] damage.

**Craft Requirements** The initial raw materials must include the scales of a giant anaconda.

**Source:** `= this.source` (`= this.source-type`)
