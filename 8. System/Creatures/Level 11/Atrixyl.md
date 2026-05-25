---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Atrixyl"
level: "11"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Aklo, Common, Draconic, Elven, Sakvroth, Thassilonian"
skills:
  - name: Skills
    desc: "Acrobatics +22, Arcana +20, Athletics +22, Deception +18, Diplomacy +18, Intimidation +20, Occultism +20, Stealth +22, Survival +16, Sinspawn Lore +20, Thassilon Lore +20"
abilityMods: ["+7", "+5", "+4", "+3", "+1", "+3"]
abilities_top:
  - name: "True Sin Scent"
    desc: "An atrixyl can smell creatures that refect or generally revel in any of the seven sins as defned by the ancient empire of Thassilon (envy, gluttony, greed, lust, pride, sloth, and wrath) within 60 feet as a precise sense and can also distinguish between diferent sins and creatures. These typically include sinspawn and certain demons, though the GM ultimately determines which creatures are appropriately sinful."
  - name: "Insectile Agility"
    desc: "When the atrixyl Leaps, High Jumps, or Long Jumps, they can increase horizontal and vertical distances traveled by up to 10 feet. They also treat falls as 50 feet shorter."
armorclass:
  - name: AC
    desc: "31; **Fort** +24, **Ref** +21, **Will** +18"
health:
  - name: HP
    desc: "190; **Immunities** controlled; **Weaknesses** acid 10; **Resistances** mental 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Spell Break"
    desc: "`pf2:r` **Trigger** The atrixyl critically succeeds on a saving throw <br>  <br> **Effect** The atrixyl shatters the portion of magic that would afect them and uses it to empower themself. The atrixyl gains temporary Hit Points equal to twice the triggering spell's rank and a +4 status bonus to damage rolls for 1 round."
  - name: "Absorb Sin"
    desc: "`pf2:0` **Trigger** The atrixyl reduces a creature it can smell with its true sin scent to 0 Hit Points <br>  <br> **Effect** The atrixyl regains 6d6 healing Hit Points."
  - name: "Improved Push"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Improved Push lists a distance, change the distance the creature is pushed on a success to that distance."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +23 (`pf2:1`) (agile, magical), **Damage** 2d12+10 bludgeoning plus [[Improved Push]]"
spellcasting: []
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The atrixyl takes on the appearance of any Medium humanoid. This doesn't change the atrixyl's Speed or their attack and damage modifers with their Strikes but might change the damage type their Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Resonating Kick"
    desc: "`pf2:2` The atrixyl makes a fist Strike. If the target is an aberration or is capable of casting spells from the arcane tradition, this attack deals an additional 2d12 force damage."
  - name: "Roundhouse Smash"
    desc: "`pf2:2` The atrixyl makes a fist Strike and compares the attack roll result to the AC of up to two foes, each of whom must be within the atrixyl's melee reach and adjacent to each other. Roll damage only once and apply it to each creature hit. This counts as two attacks for the atrixyl's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Very rarely, when sinspawn (Monster Core 310) sacrifce sentient beings to runewells, instead of sinspawn, an altogether different sort of aberration is created. Atrixyls are insectile humanoid warriors, whose powers are similar to yet stronger than ordinary sinspawn, and who are dedicated to destroying runewells and similar feshwarping artifacts. Some atrixyls seek to destroy runewells due to an imprinting of pain and suffering that occurs during their creation, seeking to prevent future suffering from runewells. Others seek to break a runewell and tap into its magical energies to gain personal power. This relentless mission has earned them the epithet "runebreakers," and brings them into confict with the sinspawn whose existences depend upon these runewells.

Atrixyls traverse Golarion's ruined wastelands in search of both ancient runewells and more contemporary feshwarping facilities.

```statblock
creature: "Atrixyl"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
