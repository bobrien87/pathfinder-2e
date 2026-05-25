---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Aftermath]]", "[[Healing]]", "[[Primal]]"]
prerequisites: "You helped to save a fey from a terrible fate, You're not a fey."
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

There are some fates worse than death–and you worked to save a fey from one such fate. In return, your life became bound to theirs. Fey magic has since become a part of you, bringing the vibrant colors of the First World to you and all that surrounds you. Your skin, hair, all that you touch, and anything within 5 feet of you changes to the most brilliant hues possible, though the colors fade as you cease to touch an object or you move away. You gain the ability to cast [[Summon Fey]] as a 7th-rank primal innate spell once per day. At 18th level the spell heightens to 8th rank, and at 20th level it heightens to 9th rank.

The first time you die after gaining this feat, the bond you made with the fey invokes the power of the First World to return you to life. Immediately after dying, you revive, becoming conscious (and wounded as normal) at 27 healing Hit Points, and you gain the fey trait. Your eyes become a rainbow of colors, and you take on a visual aspect of the fey with whom you are bound, such as by growing wings, horns, or a plantlike body. The change has no mechanical effect; for instance, the wings wouldn't allow you to fly, nor would horns grant a horn unarmed attack.

The second time you die, you reawaken in the First World with the full appearance of the fey that was bound to you. You become an NPC, unconcerned with your old mortal life. You can be returned to your previous life in the Universe by having allies spend 3 days building a shrine to the First World, giving three offerings that hold deep sentimental value for you or another, and holding a raucous, three-day long feast.

Any time that you die after that, you reawaken again in the First World with no memories of your previous life, and you can only be brought back by powerful magic such as a [[Wish]] ritual.

**Source:** `= this.source` (`= this.source-type`)
