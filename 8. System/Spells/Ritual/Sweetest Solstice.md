---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
cast: "1 hour"
targets: "a settlement with a level equal to or lower than twice the ritual's level"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

On long winter nights, many families in Tian Xia share a dish of glutinous rice balls. Wealthier families also dye these rice balls an auspicious pinkish-red in jujube juice and might serve or stuff them with expensive sweetened pastes of red beans, sesame, taro, or lotus. Sweetest solstice is a folk ritual that incorporates this tradition and allows entire villages to experience communal goodwill by celebrating a luxurious version of this dish together.

This ritual is performed over 1 hour of cooking a soup of crushed black sesame and sugar in several large cauldrons while good-natured jokes and puns praising Daikitsu, Kofusachi, and other benevolent deities are uttered; quips inspired by Hei Feng and Sun Wukong are usually included in these jovialities, for these rambunctious deities are always ready for feasts and humor. Each time a joke or pun is made, a rice ball is dropped into the boiling soups.

This ritual can only be performed once each winter season. If performed on the night of the winter solstice, the DCs of the ritual's skill checks are reduced by 2.

If the ritual is successful, the delicious black sesame soup, like the longest of nights, seems never-ending and even hides windfalls of chewy sweetness. Sometimes, this small mercy of hot meals, and the hope for pleasant surprises to come, is all a community needs to endure the bleakest of winters together.

> [!danger] Effect: Spell Effect: Sweetest Solstice
- **Critical Success** The pot contains enough black sesame soup and rice balls to feed a hot meal to everyone in the settlement for a month. The casters of the ritual gain a +1 status bonus to saves against emotion and fear effects until the end of winter.
- **Success** The pot contains enough black sesame soup and rice balls to feed a hot meal to everyone in the settlement for a week. The casters of the ritual gain a +1 status bonus to saves against fear effects for 1 month or until the end of winter, whichever comes first.
- **Failure** The ritual has no effect.
- **Critical Failure** The soup becomes tainted; it not only provides no nourishment but spreads food poisoning through the town (this might have disastrous effects). The casters of the ritual become particularly affected by illness and become [[Sickened]] 4 and can't reduce the condition for 12 hours.

**Source:** `= this.source` (`= this.source-type`)
