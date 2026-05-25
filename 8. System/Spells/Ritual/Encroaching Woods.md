---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "8"
traits: ["[[Plant]]"]
cast: "1 day"
range: "100 feet"
targets: "a section of forest no larger than 1,000 square feet"
duration: "1 week"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You entreat the spirits of a nearby wood to cloak the movements of you and your allies. Each day at dawn following the successful completion of the ritual, the trees and other plants of the affected area move up to 500 feet in a direction of your choosing. There must be enough open space for the trees to move into, maintaining the general shape and size of the affected area. Large fortifications, such as city walls, and inhospitable natural features, such as wide rivers, will stop the trees, but the forest can shape itself around small buildings and streams. The trees traverse the distance over the course of 5 minutes, which is slow enough for most creatures within the forest to move along with them if they desire. However, anyone watching the forest from outside doesn't immediately perceive the movement unless they succeed at a Perception check against the ritual's casting DC. After this movement, the fact that the trees have changed their positions is obvious.

During the ritual's duration, creatures within the forest are obscured to those outside the forest, as determined by the ritual's degree of success. This cover is usually used to stealthily approach opposing armies or settlements.

Once the ritual's duration has ended, the trees remain in their last location. They are affected normally by anything in their current environment that would prevent or stunt plant growth, such as a change of soil type or water quality, though such issues occur at the usual rate.
- **Critical Success** The affected trees sprout obscuring foliage, causing any creature within the forest to be undetected to creatures outside the forest. Each creature in the forest also gains greater cover.
- **Success** As critical success, but the creatures inside the forest are [[Hidden]] to creatures outside the forest and gain standard cover.
- **Failure** The ritual has no effect.
- **Critical Failure** The primal energy of the forest lashes out at you, cursing you to become one of the trees you sought to control. Each caster immediately gains the petrified condition, though they're solid wood instead of stone. Instead of the normal Hardness, a petrified caster has a Hardness of 5 and a weakness to axes equal to their level. The DC to counteract this condition is the ritual's casting DC.

**Source:** `= this.source` (`= this.source-type`)
