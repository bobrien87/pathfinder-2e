---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through your diligence and commitment to heroics, you finally complete your apotheosis into a true celestial. Your appearance changes as desired, becoming a perfect expression of your true self. You cease aging, and you can't die from old age. You become immune to poison and disease. You gain the celestial and holy traits, as well as the agathion, angel, archon, or azata trait, depending on whose ranks you are joining.

You become a vessel of vitality. You can cast [[Breath of Life]] once per day as a 5th-rank innate divine spell and [[Heal]] twice per day as a 7th-rank innate divine spell. When you cast a spell with the healing trait that doesn't target you, you channel this healing energy through your own body before releasing it. You regain 1d6 Hit Points per rank of the spell. In addition, you can cast [[Raise Dead]] as a 10th-rank innate divine spell. When you do, the cost to cast this spell changes to "spend 1 Mythic Point."

If you die, you're immediately reborn as a [[Nephilim]] of an ancestry of your choosing or decided in conjunction with your GM. You are descended from the celestials whose trait you bear—agathion, angel, archon, or azata. This might be represented by a lineage feat. You can choose if you will be reborn on the Universe, Elysium, Heaven, or Nirvana. Regardless of where you're reborn, celestials watch over you, keeping you safe throughout your life. When you reach the age of maturity, you regain your previous powers and memories, becoming an ascended celestial once again. These memories are faint and dreamlike, as if they happened to another person, giving you perspective and history, but not supplanting your current personality or emotional connections.

**Source:** `= this.source` (`= this.source-type`)
