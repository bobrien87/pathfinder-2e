---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
duration: "until the end of your next turn"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Sometimes the most common irritations can band together and become threats to your enemies. You reach out to the pests and nuisances around you, forming a small squadron of them to harass and occupy your opponents. They swarm from the forests, the air, and even the dirt beneath your feet. The pest squadron occupies the space of a Large creature, and like a swarm, they can occupy the same space as other creatures. When you Cast this Spell, choose one of the pest squadrons below to summon.

- **Cockroaches** Speed 30 feet, climb 30 feet.

- **Arrive** *Scurrying Swarm* The swarm of cockroaches scuttles toward the enemy, swarming them and climbing up the bodies of any enemy touching the ground. They deal @Damage[4d6[piercing]|options:area-damage] damage ([[Reflex]] save) to all enemies within their space and in a @Template[emanation|distance:5]. On a critical failure, a creature can't use concentrate actions for 1 round as they try and brush away the insects.

- **Depart** *Farewell Dirt* The cockroaches disperse, climbing down from the creatures and leaving behind their debris and dirt. All enemies in their space must attempt a [[Fortitude]] save. On a failure, a creature is [[Sickened]] 2 ([[Sickened]] 3 on a critical failure).

- **Mosquitoes** Speed 30 feet, fly 50 feet.

- **Arrive** *Biting Flight* The mosquitoes arrive in a hazy cloud, landing on the exposed skin of your opponents and dealing @Damage[4d6[piercing]|options:area-damage] damage to enemies in their space ([[Reflex]] save).
- **Depart** *Parting Gift* The swarm attempts to drain their opponents before flying off. All enemies in their space and in a @Template[emanation|distance:5] must succeed at a [[Fortitude]] save or become [[Drained]] 1 ([[Drained]] 2 on a critical failure).

- **Pigeons** Speed 20 feet, fly 40 feet.

- **Arrive** *Dive Bomb* The swarm of pigeons dives into the crowd of enemies and attacks with beaks and talons. Each enemy within their space takes @Damage[2d8[piercing],2d4[slashing]|options:area-damage] damage ([[Reflex]] save). On a critical failure, a creature is [[Dazzled]] for 1 round.
- **Depart** (sonic) *Wing Snap* The pigeon swarm snaps their wingtips together to startle their opponents before leaving. Each enemy within their space takes @Damage[4d6[sonic]|options:area-damage] damage ([[Fortitude]] save).

- **Rats** Speed 30 feet, burrow 20 feet.

- **Arrive** *Chittering Race* Rats swarm the legs of your enemies, biting at them and digging their sharp nails into whatever exposed flesh reveals itself. Each enemy in their space takes @Damage[4d6[piercing]|options:area-damage] damage ([[Reflex]] save).
- **Depart** *Underfoot* The rats scurry underfoot, tripping up enemies and burrowing underground to make a swift getaway. Each enemy in their space must succeed a [[Reflex]] save or be knocked [[Prone]] and take @Damage[2d6[bludgeoning]|options:area-damage] damage. The area the rat swarm was in becomes difficult terrain for 1 round.

- **Skunks** Speed 30 feet, climb 20 feet;

- **Arrive** *Mustelid Charge* Skunks race to the scene, and each enemy within their space and within a @Template[emanation|distance:5] take @Damage[4d6[piercing]|options:area-damage] damage ([[Reflex]] save) as the skunks snarl and bite.
- **Depart** (acid) *Stink Bomb* Before leaving, the skunks launch a final offensive maneuver and release their stink glands in a @Template[cone|distance:15]. All creatures in the area take @Damage[2d6[acid]|options:area-damage] damage ([[Fortitude]] save). On a failure, a creature is also [[Sickened]] 1 (sickened 2 on a critical failure).

- **Spiders** Speed 30 feet, climb 30 feet.

- **Arrive** (poison) *Venomous Swarm* A horde of violin spiders crawls up from the ground, climbing onto enemies within their space and in a @Template[emanation|distance:5] and biting them. Each enemy takes @Damage[3d6[piercing]|options:area-damage] damage ([[Fortitude]] save). Enemies who fail are exposed to violin spider venom.

- **Depart** *Spinning Webs* As the violin spiders depart, they spray sticky webs at their enemies in a @Template[cone|distance:30]. All creatures in this cone must attempt a [[Reflex]] save. On a failure, a creature takes a –10-foot circumstance penalty to their Speeds (–20-foot circumstance penalty on a critical failure) for 1 minute; a creature can remove this penalty with a successful [[Escape]] against your spell DC. The area of the cone is also difficult terrain for 1 round.

**Violin Spider Venom** (poison)

**Saving Throw** DC 24 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** @Damage[1d6[poison]|traits:poison] (1 round)

**Stage 2** @Damage[2d6[poison]|traits:poison] and [[Clumsy]] 1 (1 round)

**Stage 3** 2d6 poison, 1d6 persistent,bleed, and clumsy 1 (1 round)

**Stage 4** 2d6 poison, 2d6 persistent,bleed, and clumsy 1 (1 round)

**Source:** `= this.source` (`= this.source-type`)
