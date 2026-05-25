---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
traits: ["[[Trial]]"]
cast: "1 day"
source: "Pathfinder Lost Omens Tian Xia World Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The gods who value benevolence and the caretaking of small and vulnerable beings also value those qualities in the mortal adventurers who journey through the lands of Tian Xia. You demonstrate your willingness to aid even the most helpless of life by nursing a small, injured bird to health and allowing it to fly away to freedom, earning in return the protection of the natural world. If you're able to nurse the bird to health, it will return to you with a seed, which will grow into a sprout bearing a single flower.

The sprout withers if you don't personally water it with at least 1 Bulk of pure spring water a day or if it's left unattended in dangerous circumstances. It's anathema to this ritual to let the sprout wither, and doing so immediately ends its benefits. If the ritual is ended in this way, you must conduct an [[Atone]] ritual before attempting this ritual again.
- **Critical Success** As success, except the sprout also grows a single fruit after you've cared for it for a week. Removing the fruit causes the sapling to wither, but the fruit can be eaten as a Moderate Healing Potion.
- **Success** You nurse the bird to health. It returns to you with a seed that, when planted and watered, grows into a sprout with a single flower. Once you've cared for it for a week, you gain the [[Toughness]] feat. If you lose Toughness due to violating the ritual's anathema, you lose a number of Hit Points equal to the decrease in your maximum Hit Points.
- **Failure** You aren't able to heal the bird, but you help its passing to be as painless as possible.
- **Critical Failure** Your attempt to heal the bird causes greater suffering. Another bird brings you a seed that, if planted, will grow into a gourd that releases a small demon to attack you.

**Source:** `= this.source` (`= this.source-type`)
