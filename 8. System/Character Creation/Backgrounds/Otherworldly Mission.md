---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Religion"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're called to serve a specific purpose-your deity told you so, and so it must be true. Maybe you grew up knowing all along, or maybe it came to you one day in a vision, clear as a bell and twice as loud. You have some task that only you can accomplish. You mission might be as dangerous as killing a deadly tyrant or as simple as opening a particular door on a particular day. You should work with your GM on how to handle the truth of your character's backstory or leave it to the GM to decide in secret. Is this call to action a message from the character's own mind, are they being manipulated by some manner of supernatural entity, or are they actually getting marching orders from one of the deities of the setting?

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You're trained in Religion. Once per adventure, you can ask the voice you believe to be a deity for orders and get some kind of instruction-you never get any kind of explanation, simply a command to go somewhere or do something. Following those commands isn't always safe, but it's usually interesting.

**Source:** `= this.source` (`= this.source-type`)
