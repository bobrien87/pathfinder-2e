---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism, Spirit Lore Lore"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You've lived among kami, gaining a wellspring of spiritual power found deep within the Forest of Spirits. You've heard many rumors of what lies beyond the safety of your home and, for better or worse, they intrigue you. Whatever your reasons for leaving, you're still bound to whatever entity serves as your ward. Whether you return to the place of your birth or find a new land to call home is up to you.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in Occultism and Spirit Lore. You also gain a ward that binds you to a specific animal, plant, object, or location of your choice. Once per day, you can spend an Interact action to merge with your ward and heal Hit Points equal to your level. This action has the healing trait.

**Source:** `= this.source` (`= this.source-type`)
