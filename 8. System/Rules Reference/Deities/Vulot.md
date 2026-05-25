---
type: deity
source-type: "Remaster"
domains: "Confidence, Secrecy, Trickery, Delirium"
favored-weapon: "Dagger"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Befuddle]], Rank 4: [[Honeyed Words]], Rank 5: [[Portrait Of The Artist]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Vulot is the nascent demon lord of lies, loss of identity, and suffocation. The All or None receives worship from liars, con artists, opportunistic community leaders, and even some stage performers. As befits a demon lord of disguises and swapping faces, Vulot has several forms, varying from a humanoid body made up of dozens of different faces to a nondescript, mannequin-like form with no face at all. The All or None sees each identity stolen as an opportunity to consume the potential that individual holds. Vulot doesn't feed on the abstract idea of potential, instead using a person's potential to provide divine fuel for further machinations. Vulot's ultimate goal is to use all of this potential to ascend far beyond the status of demon lord into something greater, destroying or appropriating anyone else along the way, including any fellow demon lords that may act as obstacles to this goal. The demon lord's cultists tend to be individual and solitary, as covering up their identity requires few to know their true selves. Their work aims less for direct confrontation instead destroying the connections of a community through falsehoods and whisper campaigns. Luckily, the All or None's followers are generally too individualistic for more than short-term gains.

**Title** The All or None

**Areas of Concern** Disguises, lies, stolen identities

**Edicts** Steal another's identity, never introduce yourself the same way twice, use someone else's reputation to your advantage

**Anathema** Expose your unadorned face, reveal a conspiracy to the public, surrender a criminal to the authorities

**Religious Symbol** dagger lodged into wooden head

**Sacred Animal** moth

**Sacred Colors** black, gray

**Source:** `= this.source` (`= this.source-type`)
