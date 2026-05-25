---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
traits: ["[[Mythic]]"]
cast: "1 day"
range: "120 feet"
area: "30-foot burst"
targets: "area that doesn't contain any structures"
duration: "1 week"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The physical world resists changes, but this can be subdued like any other foe. The hero-god of movement and mountains, the sure-footed Helidys, found the islands of Iblydos stubborn and unwilling to bend to his will. He asked a sandbar to lower itself so his ship could pass, but it refused. He asked again, and the sandbar told him to wait for the tides to change. On his third ask, he didn't wait for a response, and instead leapt from his ship and wrestled with it. The sandbar pushed and pulled with the currents, but Helidys succeeded and flattened the sandbar into a ribbon with his bare hands.

When you cast this ritual, select to add, remove, roughen, or smooth out the area.

**Add** You create new terrain, selecting earth, stone, or water when you cast this ritual. Any creature within the newly created terrain's area moves to the closest available space. The new terrain can be created in a space that would not typically support it, such as a floating island.

**Remove** You create a 30-foot-deep crater-like depression in the area. Unless otherwise specified, the terrain immediately beneath the destroyed area is the same type. Water flows into the crater if such is present along the area's circumference. Creatures standing on the destroyed terrain can attempt to [[Grab an Edge]] if they are adjacent to a non-destroyed space. Otherwise, they use the typical rules for falling.

**Roughen** You transform the area into difficult terrain. If the area was already difficult terrain, it becomes greater difficult terrain.

**Smooth** You transform an area of difficult terrain into normal terrain, or an area of greater difficult terrain into difficult terrain.
- **Critical Success** You transform the area of your choice permanently.
- **Success** You transform the area for the ritual's duration.
- **Failure** You fail to transform the area.
- **Critical Failure** The ritual backfires, and now the land knows how to easily beat you. For the next week, the primary caster treats all instances of the terrain they attempted to manipulate as difficult terrain (or difficult terrain as greater difficult terrain).

**Heightened (+1)** The area increases by 20 feet.

**Source:** `= this.source` (`= this.source-type`)
