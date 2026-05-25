---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Artifact]]", "[[Magical]]", "[[Mythic]]"]
price: "{'value': {}}"
usage: "other"
bulk: "48"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Each *Doomsday Door* varies in appearance, yet all are gargantuan wooden portals affixed into a solid anchored arch. All *Doomsday Doors* have two methods of activation; both of these are downtime activities, and you can't pursue other downtime or exploration activities while using either activation.

**Activate—Attune Door** 1 week (concentrate, downtime)

**Effect** You attune the *Doomsday Door* to a location associated with destruction, such as the heart of an active volcano. You must know the location exists. If it is on a different plane, a planar key must be present.

Each day you spend Attuning, you must spend 1 Mythic Point or your doomed condition's value increases by 1. A creature assisting you with the rite can spend a Mythic Point instead, and you can avoid spending a Mythic Point by making an appropriate sacrifice, as determined by the GM.

After seven days, the *Doomsday Door* attunes to your chosen location, then shuts. Until then, this activity can reattune to the door to a different location. You can also use this activation to negate a *Doomsday Door*'s current attunement.

**Activate—Open Door** 1 week (concentrate, downtime)

**Requirements** The *Doomsday Door* is attuned

**Effect** You perform an extended rite to open the *Doomsday Door*. Each day you spend performing the rite, you must spend 1 Mythic Point or your doomed condition's value increases by 1. A creature assisting you with the rite can spend a Mythic Point instead, and you can avoid spending a Mythic Point by making an appropriate sacrifice, as determined by the GM.

After 7 days, the *Doomsday Door* opens, releasing an apocalypse related to the location to which the door is attuned. The consequences are determined by the GM but are always regional and far-reaching. A *Doomsday Door* attuned to the Void, for example, might release a burst of energy that causes the dead in a radius of hundreds of miles to rise from their graves.

**Destruction** A *Doomsday Door* can be destroyed by using the Attune Door activation to attune it to a specific location of great creative potential, and then Opening the Door to let this antithesis of doom flow through the portal.

**Source:** `= this.source` (`= this.source-type`)
