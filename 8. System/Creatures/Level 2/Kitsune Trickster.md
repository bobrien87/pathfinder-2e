---
type: creature
group: ["Humanoid", "Kitsune"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kitsune Trickster"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kitsune"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +8, Deception +10, Diplomacy +8, Nature +6, Performance +8, Thievery +8"
abilityMods: ["+0", "+4", "+0", "+0", "+2", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +10, **Will** +8"
health:
  - name: HP
    desc: "25"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (finesse), **Damage** 1d6+2 slashing"
  - name: "Ranged strike"
    desc: "Foxfire +12 (`pf2:1`) (fire, magical), **Damage** 1d4+2 fire"
spellcasting:
  - name: "Primal Spontaneous Spells"
    desc: "DC 0, attack +0<br>**1st** (3 slots) [[Charm]], [[Detect Magic]], [[Figment]], [[Fleet Step]], [[Light]], [[Prestidigitation]], [[Runic Body]], [[Tangle Vine]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The kitsune trickster transforms into the tailless form of a specific Medium human. The tailless form can't be altered and resembles the kitsune's fox-like humanoid form. While the kitsune trickster's alternate form is a Medium human, some kitsune have tailless forms of other humanoids, or a fox alternate form. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

With minor magic and shapeshifting capabilities, these tricksters love to play mostly harmless pranks for their own enjoyment.

Kitsune are shapeshifting, fox-like humanoids who have been blessed by the spirits. They can shift from the form of a fox-headed humanoid into a specific alternate form unique to each kitsune, usually either a tailless form—such as a humanoid body without any fox features (typically of the prevalent ancestry where they grew up)—or a fox form. Kitsune revel in joy and beauty, often practicing storytelling, dance, and other creative arts. However, they also have a penchant for playing pranks on the joyless and self-important, earning them a reputation as tricksters. Favored by the goddess Daikitsu, kitsune seem to be almost supernaturally lucky, perpetually dodging danger by the narrowest margins.

While kitsune settlements do exist, most kitsune are incredibly curious and often leave home at a young age to encounter new people and sights. Some kitsune spend years in their tailless form, living disguised among humanoids in urban or rural societies whose inhabitants have no clue of their true nature. Others go to the opposite extreme, spending most of their lives in the form of a fox, only to reveal themselves at the most opportune moment. For many kitsune, revealing their true form to someone is a sign of great trust, but it's also not uncommon for kitsune to display their dual nature openly.

Kitsune's connection to the spiritual world grants them a number of magical abilities. Aside from their innate shapeshifting powers, kitsune naturally develop more potent magic as they mature, and they seem to effortlessly pick up skills that would rival the most practiced spellcasters. Those who truly apply themselves to honing their magic usually become remarkable at their craft.

A kitsune is born with one tail, but as their magical powers grow, so do their number of tails. Elders blessed with great magical wisdom can have as many as nine, though according to popular legend, this level of power can take up to a thousand years to achieve.

```statblock
creature: "Kitsune Trickster"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
