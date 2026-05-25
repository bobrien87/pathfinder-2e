---
type: background
source-type: "Remaster"
traits: ["[[Persona underdog]]"]
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Games Lore Lore"
feats: "[[Streetwise]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

When you were young, for whatever reason, you were always the last pick when it came to choosing teammates for a game, selecting someone for an important job, or the final person in your social circle to achieve an important milestone. As a result, you've come to expect being overlooked, and that's helped to shape your worldview. Maybe you take advantage of this to get away with things that no one would suspect you of, or perhaps it has encouraged you to focus on your training and become even better at what you do. Nothing's worked, exactly, but that's just left you with more time to watch and learn how everyone else behaves, which has given you greater insights into the societies that always seem to forget about you. You've studied the rules of countless games and competitions so that you're always ready to capitalize on a technicality to make up for being regarded as a weak link. When you do succeed at a task, it's often to the surprise of observers, and it's happened enough by now that there are those who, perhaps as a result of also always being chosen last, have come to view you as an inspiration to look up to.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Society skill and the Games Lore skill. You gain the [[Streetwise]] skill feat.

If you have the Underdog persona trait, you also become trained in the Scouting Lore skill.

**Source:** `= this.source` (`= this.source-type`)
