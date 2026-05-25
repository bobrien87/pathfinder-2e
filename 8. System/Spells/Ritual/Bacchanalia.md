---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
traits: ["[[Emotion]]", "[[Mental]]"]
cast: "1 day"
duration: "until midnight (see text)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You hold an elaborate feast and stoke the celebratory spirit, causing it to spread to other people nearby; you buoy them with hope and good cheer as they revel into the night. The ritual was first developed by the cult of the hero-god Kelksiomides in Iblydos and meant to be a benefit to the community during hard times, though other groups have used it for far different purposes, such as to spread chaos or to provide cover for a heist.

You and the secondary casters begin your feast in a public space where others can see you, exactly 8 hours before dusk. When dusk falls, you complete the ritual. The party spreads outward from your initial site until it slowly encompasses the settlement (for a town or smaller), or a district or division of up to approximately 1,000 people (for a larger settlement). Those partaking in the celebration are [[Fascinated]] until the ritual comes to an end (or someone uses a hostile action toward them, as usual). The partying appears to spread naturally, as others see the revelers, they too slowly join until the celebration reaches its peak size. The spell's effect ends sharply at midnight, but that doesn't mean people stop partying right away if they're enjoying themselves.
- **Critical Success** The party is a huge hit! The effects work as above, except that in a larger settlement, the celebration can spread to an area with as many as 10,000 people. Furthermore, the celebration leaves strong memories in the hearts of those who participated, causing locals to commemorate it or possibly outlaw such celebrations (depending on their view of the event).
- **Success** The party is successful. It spreads as described in the ritual's description.
- **Failure** The party never really catches on. You and the secondary casters get to celebrate, but the most other people do is give you odd looks.
- **Critical Failure** Instead of celebration, you inspire anger and resentment toward you and the secondary casters for disturbing the peace or possibly even deepening the despair of a people who are already troubled. People in the area have their attitudes toward you temporarily adjusted two steps worse than normal. Those who become hostile won't necessarily attack you, but they will mock you, break up your revelry, and potentially arrest you.

**Source:** `= this.source` (`= this.source-type`)
