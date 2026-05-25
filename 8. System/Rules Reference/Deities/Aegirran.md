---
type: deity
source-type: "Remaster"
domains: "Air, Dreams, Travel, Water"
favored-weapon: "Trident"
divine-font: "Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 3: [[Aqueous Orb]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Predominantly worshipped by tide giants, Aegirran is venerated as the god of dreams, sailing, and ocean voyages. Despite being wed to Skode, he is forever separated from her except for during the brief changing of seasons when his coral-covered ship touches upon the shore. For the rest of the year, he is leading nine daughters (the gentle yet free east, south, and west winds) he bore with his wife on an endless journey across and below the seas, bringing rain and sunshine to the seaboard and inland fields. A hopeless romantic, he watches over the oceans. Most giant art depicts Aegirran as a tide giant, a giant with pale-blue skin and several markings reminiscent of waves. He is clad in a simple, asymmetrical cloak and sailing attire.

**Title** The Sea Dreamer

**Areas of Concern** Dreams, sailing, voyages

**Edicts** Sail the seas, offer a place for weary travelers to rest their heads, love and respect those you're in relationships with

**Anathema** Betray a loved one's trust, kill someone while they sleep, purposely pollute natural bodies of water

**Religious Symbol** spouting whale

**Sacred Animal** whale

**Sacred Colors** blue, gray

**Source:** `= this.source` (`= this.source-type`)
