---
type: creature
group: ["Monitor", "Protean"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Keketar"
level: "17"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Monitor"
trait_02: "Protean"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]]"
languages: "Chthonian, Empyrean, Protean (Telepathy 100 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +26, Athletics +33, Deception +32, Diplomacy +34, Intimidation +34, Religion +30, Stealth +30"
abilityMods: ["+8", "+5", "+7", "+5", "+7", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Entropy Sense (Imprecise) 60 feet"
    desc: "A keketar can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[Veil of Privacy]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Reshape Reality"
    desc: "When the keketar casts [[Mirage]], it infuses the illusion with quasi-real substance. Creatures that do not disbelieve the illusion treat structures and terrain created through the spell as though they were real, ascending illusory stairs, becoming trapped by illusory quicksand, and so on."
  - name: "Warpwave Strike"
    desc: "A creature struck by a keketar's jaws or claw Strike must succeed at a DC 36 [[Fortitude]] save or be subject to a Warpwave."
armorclass:
  - name: AC
    desc: "40; **Fort** +30, **Ref** +28, **Will** +34"
health:
  - name: HP
    desc: "260; fast healing 10; **Resistances** precision 10, protean anatomy 25"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Fast Healing 10"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Protean Anatomy 25"
    desc: "A keketar's vital organs shift and change shape and position constantly. Immediately after the keketar takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. <br>  <br> The keketar is immune to polymorph effects unless they're a willing target. If [[Blinded]] or [[Deafened]], the keketar automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones. <br>  <br> > [!danger] Effect: Protean Anatomy"
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Spatial Riptide"
    desc: "30 feet. <br>  <br> A creature using a teleportation ability within the aura or arriving in it via teleportation must succeed at a DC 38 [[Fortitude]] save or wink out of existence for 1d4 rounds before completing the teleport. The creature can't act, sense anything, or be targeted. On a successful save, the creature completes the teleport normally but is [[Stunned]] 1. <br>  <br> Keketars are immune to this effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +33 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 3d12+16 piercing plus [[Warpwave Strike]]"
  - name: "Melee strike"
    desc: "Claw +33 (`pf2:1`) (agile, magical, reach 10 ft., unarmed), **Damage** 2d12+16 slashing plus [[Warpwave Strike]]"
  - name: "Melee strike"
    desc: "Tail +33 (`pf2:1`) (reach 15 ft.), **Damage** 2d12+16 bludgeoning plus [[Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42, attack +32<br>**9th** [[Unfathomable Song]]<br>**7th** [[Warp Mind]]<br>**6th** [[Cursed Metamorphosis]], [[Disintegrate]], [[Teleport (At Will, Self Only)]]<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Confusion]], [[Confusion]] (At Will), [[Creation]] (At Will), [[Divine Wrath]], [[Mirage (See Reshape Reality)]], [[Translocate]], [[Translocate]] (At Will), [[Unfettered Movement]] (Constant)<br>**2nd** [[Dispel Magic]] (At Will), [[Shatter]] (At Will)"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The keketar can take the appearance of any Huge or smaller creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d10+15)[bludgeoning]], DC 42 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The ruling caste of the proteans, keketars orchestrate attacks against the bastions of law and adjudicate protean disputes confidently and capriciously. A keketar resembles a shimmering, serpentine creature with spines, claws, and a dragon-like head. A keketar's actual appearance is in constant flux, but they generally stay about 18 feet long with a weight of around 1,500 pounds. While their physical forms can vary, two things remain constant: first, a keketar's eyes are always a piercing shade of amber or violet. Second, the keketar's mark of office—a crown of shifting symbols that hovers above their head—never changes. A keketar cannot remove their crown but can suppress it, although most are loath to do so and consider such an act one of cowardice or shame.

Keketars fill a role in protean society of a sort of priesthood, operating as intermediaries between the other proteans and the Speakers of the Depths. All other proteans defer to keketars, treating them in a way similar to how citizens of a mortal city would treat respected nobles; even more powerful proteans defer to the will of the keketars. As with many religions, dogma and theology are prone to interpretation and change, and among the proteans, the situation is even more pronounced. Whatever the nature and desires of the Speakers of the Depths may be, individual keketars often come to dramatically different conclusions as to their will and intent. To the proteans, however, this inherent dissonance is a strength rather than a weakness.

Guardians of disorder and natives of the primal plane of chaos known as the Maelstrom, proteans consider it their calling to spread bedlam and hasten entropic ends. The most powerful proteans are demigods known collectively as the protean lords, although they are mysterious entities whose cults in the Universe tend to be obscure and secretive.

Proteans divide themselves into a loose caste system and possess a dizzying variety of powers. Most proteans have a serpentine body with the head of a primeval beast. Scholars have long been intrigued by this fact—that scions of dissolution and disorder would share so many features—pointing out that there is some semblance of order even in the purest chaos. Others note that the serpentine form is one of the most primeval shapes, perhaps suggesting that in a reality at the dawn of time, such shapes were all that could exist. The proteans themselves have little to say on the matter, which, perhaps ironically, only adds to the confusion and lack of consensus surrounding their kind. After all, if even chaos cannot be trusted to be chaotic, would that not be the purest form of entropy?

```statblock
creature: "Keketar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
