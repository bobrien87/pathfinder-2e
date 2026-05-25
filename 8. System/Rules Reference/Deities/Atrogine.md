---
type: deity
source-type: "Remaster"
domains: "Ambition, Knowledge, Magic, Trickery"
favored-weapon: "Nails, Sickle"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Summon Animal]], Rank 4: [[Mirror'S Misfortune]], Rank 7: [[Retrocognition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Atrogine (uh-TROE-gin-ee) is a young god. Born of the wishes and dreams of a reclusive coven of witches, it's said Atrogine awoke in a forest that had recently been ravaged by wildfires. Saddened by the desolate landscape, their tears touched the ground and brought life back to the flora and fauna, manifesting a lush, vibrant new ecosystem. Whispers on the wind claim that Atrogine has two siblings: one the arbiter of dreams, the other the arbiter of nightmares. Not much is known of these siblings' origins, only that both share the mischievous nature of Atrogine. Rumor says the three deities have formed a coven of their own.

Atrogine is endlessly curious and voracious when it comes to the knowledge of magic. They reward this hunger and passion in their followers by imparting their own discoveries in ways both mysterious and blatant. They are also highly concerned with their followers' personal journeys. Atrogine also has quite the mischievous streak. Their curiosity leads them to rather creative means of information-seeking—they have, for instance, made a small name for themself by impersonating Pharasma and Nethys and appearing to the other gods' followers to learn more about the deities and their worshippers alike. This, naturally, begs the question: what other gods have they impersonated?

**Title** Thought Made Flesh

**Areas of Concern** curiosity, familiars, manifestation, witches

**Edicts** push the boundaries of known magic, seek like-minded community, commit to truth

**Anathema** compromise yourself for the sake of fitting in, enforce gender norms or stereotypes, withhold magical knowledge for personal gain

**Religious Symbol** eye formed by nightshade plants

**Sacred Animal** moth

**Sacred Color** purple

**Source:** `= this.source` (`= this.source-type`)
