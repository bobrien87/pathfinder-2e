---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
cast: "1 hour"
range: "30 feet"
targets: "yourself and the secondary casters"
duration: "8 hours"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

It's said that after his demise at the hands of jealous Fumeiyoshi, Tsukiyo's corpse was left unguarded; this provided a humble matron-rat opportunities to nibble at god flesh, a meal that transformed her into Lao Shu Po. Gnaw at the moon, an obscure folk magic ritual popular among Shenmen's downtrodden, allows you to honor the Old Rat Woman's audacity and unlikely ascent.

This ritual can only be performed on a night when the moon is visible in the sky above; you can't perform this ritual during a totally moonless night, while indoors, or while underground. Performing this ritual on the night of the full moon reduces the DCs of the ritual's skill checks by 2. You set out offerings of mooncakes and cups of tea on a flat surface (such as a table or a tray on the floor), assiduously ignore this food and drink, and praise the night's beauty while admiring and thanking the moon.

At the end of a successful ritual, bite marks appear on the mooncakes, and some of the tea disappears as if sipped while no one was looking. Supposedly, the ritual and offerings gain Lao Shu Po's attention, who sends her rodent children to eat and drink their fill and grant stolen blessings of moonlit sight. The effusive admiration for the moon is said to avert Tsukiyo's displeasure for commemorating the event of his murder; after all, old tales warn against giving offense to the moon, lest it slice your ears in retribution.
- **Critical Success** The targets gain darkvision.
- **Success** The targets gain low-light vision.
- **Failure** The ritual has no effect.
- **Critical Failure** You and the targets are [[Drained]] 1 for 24 hours. Your ears feel lacerated and raw as your earlobes become crisscrossed with tiny cuts.

**Source:** `= this.source` (`= this.source-type`)
