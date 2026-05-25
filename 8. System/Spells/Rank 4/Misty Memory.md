---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "1 minute"
targets: "1 body of water of at least 5 square feet"
duration: "10 minutes (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Some say water holds memories or impressions of the past, and you can raise those memories to the surface to glimpse recent events. When you Cast the Spell, you fix your mind on an amount of time in the past, up to 24 hours ago. A mist rises from the target body of water, filling a @Template[burst|distance:30] and coalescing into a misty scene of the events that took place at that time within 60 feet of the water.

Any creature who can see the area can observe the images produced, which are a translucent white color and detailed enough to show a silhouette, outline, or contour of creatures and objects that passed through the area and the motions they took. Fine details, such as facial features or written letters, are too precise for the mist to form, and the scene is silent.

You can Sustain the spell to cause the mist to play events backward or forward, with each minute spent Sustaining corresponding to a minute of playback.

Strong winds from a magical source can disrupt this spell if the effect succeeds at a counteract check against your spell DC.

**Source:** `= this.source` (`= this.source-type`)
