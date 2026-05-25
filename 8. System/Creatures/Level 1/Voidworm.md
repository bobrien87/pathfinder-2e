---
type: creature
group: ["Monitor", "Protean"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Voidworm"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Monitor"
trait_02: "Protean"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Darkvision]]"
languages: "Chthonian, Protean"
skills:
  - name: Skills
    desc: "Acrobatics +7, Deception +6, Religion +4, Stealth +7"
abilityMods: ["-1", "+4", "+0", "-1", "-1", "+1"]
abilities_top:
  - name: "Entropy Sense (Imprecise) 30 feet"
    desc: "A voidworm can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[Veil of Privacy]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Confounding Lash"
    desc: "A creature hit by the voidworm's tail Strike is [[Stupefied 1]] for 1 round ([[Stupefied 2]] on a critical hit). A successful DC 16 [[Will]] save negates this effect and grants temporary immunity to confounding lash for 1 minute."
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "16; fast healing 1; **Resistances** precision 3, protean anatomy 5"
abilities_mid:
  - name: "Fast Healing 1"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Protean Anatomy 5"
    desc: "A voidworm's vital organs shift and change shape and position constantly. Immediately after the voidworm takes acid, electricity, or sonic damage, they gains the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the voidworm takes damage of one of the other types (in which case its resistance changes to match that type), whichever comes first. <br>  <br> The voidworm is immune to polymorph effects unless it is a willing target. If [[Blinded]] or [[Deafened]], the voidworm automatically recovers at the end of its next turn as new sensory organs grow to replace the compromised ones. <br>  <br> > [!danger] Effect: Protean Anatomy"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (finesse, magical, unarmed), **Damage** 1d8+1 piercing"
  - name: "Melee strike"
    desc: "Tail +9 (`pf2:1`) (finesse, magical), **Damage** 1d4 + 1 slashing plus [[Confounding Lash]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16, attack +8<br>**4th** [[Read Omens]], [[Unfettered Movement]] (Constant)<br>**2nd** [[Blur (Self only)]], [[Mist]]<br>**1st** [[Figment]], [[Light]], [[Prestidigitation]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The voidworm takes on the appearance of a Tiny animal. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Other proteans don't consider the flying, iridescent beings known as voidworms to be part of a protean caste at all, but instead merely a shameful side effect of the Maelstrom's constantly churning energy. To call a voidworm a protean in the presence of a more powerful protean is a sure a way to instigate combat.

Voidworms themselves have little interest in whether anyone sees them as proteans. They maintain a thriving ecology in the Maelstrom, frolicking in schools of up to 20 and playing in the chaos of constantly shifting realities. Elsewhere (such as in the Universe), voidworms are mesmerized by the principle of object permanence; many latch onto specific features of a region (such as a hillside or pond) and flit through the air around it for months or even years as they wait for the object of their curiosity to change. Minor changes—such as a tree's change of color in the fall, a corpse's slow decay, or periodic venting of steam from a geyser—all fascinate voidworms. A voidworm is about 2 feet long and weighs 2 pounds.

Guardians of disorder and natives of the primal plane of chaos known as the Maelstrom, proteans consider it their calling to spread bedlam and hasten entropic ends. The most powerful proteans are demigods known collectively as the protean lords, although they are mysterious entities whose cults in the Universe tend to be obscure and secretive.

Proteans divide themselves into a loose caste system and possess a dizzying variety of powers. Most proteans have a serpentine body with the head of a primeval beast. Scholars have long been intrigued by this fact—that scions of dissolution and disorder would share so many features—pointing out that there is some semblance of order even in the purest chaos. Others note that the serpentine form is one of the most primeval shapes, perhaps suggesting that in a reality at the dawn of time, such shapes were all that could exist. The proteans themselves have little to say on the matter, which, perhaps ironically, only adds to the confusion and lack of consensus surrounding their kind. After all, if even chaos cannot be trusted to be chaotic, would that not be the purest form of entropy?

```statblock
creature: "Voidworm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
