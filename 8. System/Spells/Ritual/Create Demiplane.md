---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]", "[[Teleportation]]"]
cast: "9 days"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Few incantations are as renowned as the power to create worlds. To cast this ritual, you must be on the Astral Plane, the Ethereal Plane, or a plane that connects to one of the two. A demiplane created with this ritual exists on the Astral or Ethereal Plane. It can have the appearance of any mundane environment or structure, such as a glorious cathedral, a forest clearing, a comfortably furnished cavern, or anything else imaginable. All demiplanes have finite, unbreachable boundaries, which might resemble stone, wood, or something more unnatural, such as a wall of mist or unceasing void.

Demiplanes have environmental conditions appropriate for the Universe, though the primary caster can dictate a general climate or light level as well as whether the demiplane experiences seasons or a day-night cycle. The demiplane has no native plants or animals, but they can be introduced, and plants will grow in a demiplane's light.

When you first cast *create demiplane*, the casters are teleported to the demiplane. The demiplane has no direct access to other worlds, so [[Interplanar Teleport]] or similar abilities are necessary to access it. As part of casting the ritual to create a new demiplane, you create a planar key to the demiplane that serves as an *interplanar teleport* locus for that demiplane. Most resemble ornate keys, but some take the form of maps, compasses, or dowsing rods.

If you have the original planar key to an existing demiplane and are also on that demiplane, you can cast this ritual again. Each time, you can either expand the demiplane's size or add one special trait or feature described below.

- **Bounteous** The demiplane has a functional ecosystem with plants and animals appropriate to the environment. This ecosystem doesn't require any additional effort on your part to maintain.
- **Elemental** The demiplane gains the air, earth, fire, metal, water, or wood planar essence trait.
- **Gravity** The demiplane gains a gravity trait of your choice.
- **Key** You create an additional planar key that can be used to access the demiplane with *interplanar teleport* and improve it with *create demiplane*.
- **Portal** You create a permanent gateway between the demiplane and a single other location. You must spend the ritual's casting time constructing the gateway on the external side, which typically resembles an arch or doorway of some sort. The gate is always active, but it can be secured as you would any door.
- **Scope** The demiplane can be unbounded instead of finite, though still with the same size.
- **Critical Success** You create a new demiplane whose area consists of 10 contiguous squares, each 100 feet on a side. The ceiling is 40 feet high. If modifying an existing demiplane, you can instead either add this area to the demiplane's size or add two special traits or features.
- **Success** As critical success, but the demiplane's area is two squares, each 100 feet on a side, with a ceiling 20 feet high. If modifying an existing demiplane, you can add one special trait or feature.
- **Failure** The ritual has no effect.
- **Critical Failure** Something goes horribly wrong, and all casters are teleported to an unknown but hostile plane.

**Heightened (10th)** The ritual creates a square area 2,000 feet on a side, with a ceiling 60 feet high (or two contiguous areas of this size on a critical success). The cost of the ritual increases to 20,000 gp.

**Source:** `= this.source` (`= this.source-type`)
