---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism, Demon Lore Lore"
feats: "[[Trick Magic Item]]"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The power stories exude over the world has long fascinated you. No matter if they're accurate historical accounts, distorted parables, or completely fictional constructions, the way tales can shape society is a kind of magic. In some cases, literal, occult magic! One tale that's come back to modern lips of late is an ancient one indeed, the story of the elven hero Iyalirrin, an Ekujae bard who helped to create a ritual known as the anima invocation in his people's pursuit against the devastations caused by Dahak in the aftermath of Earthfall. Other heroes rediscovered Iyalirrin's story and the ritual a few short years ago, but it was Iyalirrin's admiration of the art of storytelling that spoke more to you. Whether you came to this realization recently or if you've long known about the ancient elven hero's admiration of spoken tales, you've devoted much of your adult life to the gathering and crafting of stories of your own. The way in which occult magic can manipulate the power of story is a particular obsession of yours, especially with a handy little trick you've learned that allows you to access power locked away in magic items you'd otherwise struggle to use. Simply by adjusting your story, the item's story, or both... and then giving the tiniest little push of occult magic, you can unlock a wide range of magical tools. These same tricks, you've come to discover, also work well on demons—particularly when used to remind them of their sins and the shame their once-mortal souls may have held eons ago.

Choose two attribute boosts. One must be to **Charisma** or **Intelligence**, and one is a free attribute boost.

You're trained in the Occultism skill and the Demon Lore skill. You gain the [[Trick Magic Item]] skill feat, as well as the [[Opportunistic Accusation]] reaction.

**Source:** `= this.source` (`= this.source-type`)
