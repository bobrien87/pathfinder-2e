---
type: creature
group: ["Fiend", "Sahkil"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kimenhul"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+35; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +36, Arcana +33, Athletics +34, Deception +38, Occultism +33, Religion +35, Stealth +36"
abilityMods: ["+10", "+8", "+9", "+5", "+7", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Easy to Call"
    desc: "A kimenhul's level is considered 2 lower for the purpose of being conjured by the [[Binding Circle]] ritual (and potentially other rituals, at the GM's discretion), but it is always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Snatch Between"
    desc: "When using Skip Between, the kimenhul can bring along any creatures it has [[Grabbed]]."
  - name: "Unsettled Mind"
    desc: "Any creature affected by any of a kimenhul's mental spells or abilities becomes [[Stupefied 3]] for the duration of that effect and for 1d4 rounds thereafter."
armorclass:
  - name: AC
    desc: "45 all-around vision; **Fort** +33, **Ref** +32, **Will** +35"
health:
  - name: HP
    desc: "425; **Immunities** death effects, fear effects; **Weaknesses** holy 20"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Feed on Fear"
    desc: "The kimenhul regains 30 healing Hit Points at the start of its turn as long as any [[Frightened]] creature is within @Template[emanation|distance:100]{100 feet} of it."
  - name: "Reactive Strike (Special)"
    desc: "`pf2:r` If the triggering creature is frightened, the kimenhul can make two claw Strikes against the creature instead of one Strike. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +38 (`pf2:1`) (magical, reach 15 ft., unarmed, unholy), **Damage** 4d12+18 piercing plus 3d6 spirit"
  - name: "Melee strike"
    desc: "Claw +38 (`pf2:1`) (agile, magical, reach 15 ft., unarmed, unholy), **Damage** 4d8+18 slashing plus 3d6 spirit plus [[Improved Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42, attack +34<br>**9th** [[Phantasmagoria]]<br>**8th** [[Hidden Mind]] (Constant)<br>**7th** [[Mask of Terror]] (At Will), [[Warp Mind]]<br>**6th** [[Phantasmal Calamity]], [[Truesight]] (Constant)<br>**4th** [[Confusion]], [[Suggestion]] (At Will)<br>**2nd** [[Dispel Magic]] (At Will)<br>**1st** [[Detect Magic]], [[Fear]] (At Will)"
abilities_bot:
  - name: "Eternal Fear"
    desc: "`pf2:2` The kimenhul contorts its faces and presents itself to its enemies in a terrifying and traumatic display that causes lingering fear. Each creature within 100 feet that can observe the kimenhul must make a DC 42 [[Will]] save. <br>  <br> They are then temporarily immune for 10 minutes. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target becomes [[Frightened]] 3. <br> - **Failure** The target becomes [[Frightened]] 3 and is [[Fleeing]] as long as it's frightened. Even after recovering from the initial experience, the trauma is lodged in the target's mind for 1 year. Once per day, the kimenhul can communicate telepathically with the target for 1 minute as long as both creatures are on the same plane. Any time a creature under the effect of Eternal Fear is in a stressful situation (such as combat or intense social pressure), they must succeed at a DC 11 flat check or become [[Frightened]] 2. While Eternal Fear lasts, the target always becomes fleeing as long as it's frightened, regardless of the source of the fear. The target can attempt a new saving throw each week to remove these effects, but they can otherwise be removed only by powerful magic such as [[Wish]]. <br> - **Critical Failure** As failure, but the effects are permanent and the target doesn't get to attempt a weekly save to end the effect."
  - name: "Frightening Flurry"
    desc: "`pf2:2` The kimenhul makes one jaws Strike and two claw Strikes against a single target, in any order. The target becomes [[Frightened]] with a condition value equal to the number of Strikes that hit it, to a maximum of frightened 3 if all three Strikes hit."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
  - name: "Skip Between"
    desc: "`pf2:1` The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Among the strongest of their kind aside from the sahkil tormentors, kimenhuls work their craft to foment despair in those who fear failure, forming cycles of self-loathing. These powerful sahkils focus their attention on mortals who are seemingly at the peak of their ability yet harbor secret fears of inadequacy. A kimenhul's predations can leave an indelible mark on its victims. The kimenhul whispers threats and sends fears of crushing failure to its prey, seemingly originating from their own minds, a trauma that can be difficult to bear without help. These sahkils torment their prey as long as the hapless victims live, using their Eternal Fear ability every day to psychically remind their previous victims of their failings.

Some unique kimenhuls find themselves in a position of leadership in Xibalba, where they carve out their own small kingdoms and direct groups of sahkils to help them find mortals to torment. They rule these nightmare kingdoms through terror, often delighting in tormenting new petitioners or scheming ways to work against their immortal foes.

Ages ago, when this cycle of the multiverse was still adolescent, a cabal of psychopomps who already felt bored and restrained in their role of ushering souls to their ultimate resting place rebelled against their station. It was this corruption of the cycle of souls that spawned the first sahkils.

Ambivalent to the prescribed order of the multiverse and spiteful of mortals, sahkils delight in spreading fear and unease to all beings, clogging up the metaphysical cycle with anxiety-ridden mortals too scared to achieve their potential. These fiends have drastically changed from their dedicated psychopomp predecessors. They are creatures of spite and torment, fear and disgust. They exploit the most common and rare fears for their own perverse satisfaction, and they want nothing more than to frighten mortals and make them question their reason for existence.

Most sahkils lurk on the Ethereal Plane, but they frequently invade the Material Plane to torment mortals and spread terror. They use their innate ability to slip between the veils of the Ethereal and Material effortlessly, often stalking their targets for days or weeks before enacting their devious plots.

```statblock
creature: "Kimenhul"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
