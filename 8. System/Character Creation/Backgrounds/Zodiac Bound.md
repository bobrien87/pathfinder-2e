---
type: background
source-type: "Remaster"
boosts: "Cha/Con/Dex/Int/Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Astrology Lore Lore"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Fortune tellers and oracles claim that a person's zodiac sign influences their personality and fate, and while it might not be true for all, it seems true for you. You were born under a powerful manifestation of a specific constellation, corresponding to a symbol of the zodiac. When you gain this background, choose a specific constellation from those listed below. Your associated constellation determines one of the attribute boosts you gain and an innate spell. The list includes benefits for the constellations of the Dragon Empires Zodiac, but you might have been born under a different constellation and gain different benefits as determined by the GM.

Choose two attribute boosts. One must be to the attribute tied to your sign, and one is a free attribute boost.

You're trained in Astrology Lore. You also gain the ability to cast a divine innate spell, as determined by your sign. The frequency with which you can cast this spell is listed below; cantrips can be used as often as you wish. As normal, you cast non-cantrip innate spells at the lowest rank available to that spell, such as 2nd rank for *water breathing*, and cantrips are heightened to half your level. Additionally, once during the prominent time for your sign (typically once per year), you can cast your sign's spell without expending its normal use.

**The Underworld Dragon (Intelligence)**: [[Ignition]]; at will

**The Swordswoman (Dexterity)**: [[Gale Blast]]; at will

**The Sea Dragon (Constitution)**: [[Water Breathing]]; once per week

**The Swallow (Dexterity)**: [[Jump]]; once per day

**The Ox (Strength)**: [[Ant Haul]]; once per day

**The Sovereign Dragon (Charisma)**: [[Command]]; once per day

**The Ogre (Strength)**: [[Fear]]; once per day

**The Forest Dragon (Wisdom)**: [[Tangle Vine]]; at will

**The Blossom (Charisma)**: [[Dizzying Colors]]; once per day

**The Dog (Constitution)**: [[Clear Mind]]; once per week

**The Sky Dragon (Intelligence)**: [[Bless]]; once per day

**The Archer (Dexterity)**: [[Sure Strike]]; once per day

**Source:** `= this.source` (`= this.source-type`)
