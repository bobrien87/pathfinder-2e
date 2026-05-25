---
type: deity
source-type: "Remaster"
domains: "Creation, Wyrmkin, Fate, Time"
favored-weapon: "Jaws, Sling"
divine-font: "Harm, Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Mindlink]], Rank 3: [[Enthrall]], Rank 5: [[Summon Dragon]], Rank 9: [[Unfathomable Song]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In a time before time, Sarshallatu was endless, like a great sea spreading out into the infinite horizon. She knew only that she existed and in the untethered reaches of mind unbound by trappings of physicality, she considered the idea of the self—and in the flickering moment in which she wondered if there might be more to her than the infinite that she was, she glimpsed something new. Something beyond herself, beyond her conception, beyond her perception. She laughed, and it thundered across what would become creation, for this something new was another being. She would call him the Waybringer, Apsu, and by indulging in his existence the infinite became finite and Sarshallatu ceased to be endless.

With Apsu came time, and it was a wonderful thing. It would give Sarshallatu memories to cherish. It gave her hope and trepidation for all that might come in time; a mate, a clutch of offspring, a cosmos to craft to their whims, worlds to paint with all potentialities of what could someday be. The infinite within the finite, the greatest gift she had ever conceived of, for all beings now to share.

But with time came change as well, and the laughter of eons would see a being once infinite learn about loss. Apsu and she would produce a clutch of offspring, but they were sadly lesser. They played vicious games and made countless calamities. They would fight and they would die, and from these losses, Sarshallatu learned contempt.

She pulled back from her offspring and her love, to shy away from the world of Golarion which she had hoped would have been their grandest endeavor. She had chosen to be finite, to be known, to be of a state of being which no longer encompassed all things. To be something other than something that simply is. And once more she laughed, for she realized she was the cause of her suffering as much as she was the catalyst for her joys. The song of her laughter rumbled like thunder across creation, rattling the cosmos.

**Title** The Thundering Song

**Areas of Concern** dragons, potential, reality

**Edicts** feel privileged to witness wonders of creation, find value in being, change to better know yourself

**Anathema** change yourself for another, be consumed by temporary things, let others define your soul

**Religious Symbol** sun wheel composed of serpents

**Sacred Animal** all

**Sacred Colors** none

**Source:** `= this.source` (`= this.source-type`)
