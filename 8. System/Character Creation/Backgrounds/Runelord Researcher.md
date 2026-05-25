---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Arcana, Academia Lore Lore"
source: "Pathfinder Revenge of the Runelords Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

For thousands of years, the looming monoliths found throughout the Saga Lands were a source of pride, fear, and curiosity, yet the dangers associated with them and the gulf of time itself kept their secrets mostly hidden. When Runelord Karzoug rose from his eons-long slumber in 4707 ar, these ancient secrets became thrust into the light, and Thassilon's legacy became a topic of modern discussion and exploration. The foundation of New Thassilon only strengthened this shift, and now you're one of many who have devoted your studies on the deep history of Thassilon and its runelords—a topic still shrouded in mystery. Whether the focus of your studies has been one of the more recently active runelords, like Karzoug, Alaznist, Belimarius, or Sorshen, or you're focused on one of the more obscure dozens of runelords who ruled during the centuries Thassilon existed, your knowledge has made you an invaluable asset on many adventures in the Saga Lands. It's also attracted Queen Sorshen's attention, and in her invitation to attend the opening ceremonies for the Circle of Open Hands, she made it clear she wants to engage you in several long discussions about the truths of ancient Thassilon, impressing upon you that while the runelords (including herself, she admits) of the ancient era were cruel and domineering, that many of the wonders they created could benefit the modern age–if people could trust that these wonders were safe! With your aid, she hopes to bring these innovations back.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and the other is a free attribute boost.

You're trained in Arcana and Academia Lore. When you [[Recall Knowledge]] about runelords or ancient Thassilon, you gain a +2 circumstance bonus to the check. You automatically recognize the name and time of rule of any runelord you encounter or see an accurate representation of (such as a painting or statue). In addition, during your daily preparations, you can choose one of the following schools of Thassilonian rune magic to focus your mind on, gaining a +1 status bonus to saving throws against the listed effect for the next 8 hours.

- **Envy** any effect that has the incapacitation trait (against foes who are higher level than you, the status bonus increases to +2)
- **Gluttony** death effects and void
- **Greed** polymorph and effects that can cause the following conditions: enfeebled, clumsy, or petrified
- **Lust** emotion
- **Pride** illusion
- **Sloth** effects that cause paralysis, slow, stun, or that grant penalties to your Speed
- **Wrath** effects that cause acid, cold, electricity, fire, or sonic damage (choose one)

> [!danger] Effect: Runelord Researcher

**Source:** `= this.source` (`= this.source-type`)
