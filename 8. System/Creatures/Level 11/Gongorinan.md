---
type: creature
group: ["Fiend", "Qlippoth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gongorinan"
level: "11"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: "Chthonian (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +23, Athletics +23, Intimidation +21, Stealth +21"
abilityMods: ["+6", "+6", "+7", "+1", "+3", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Gongorinan Venom"
    desc: "**Saving Throw** DC 30 [[Fortitude]] save <br>  <br> **Stage 1** [[Stupefied 1]] and cosmetic signs appear of turning into an animal, fungus, or plant (1 round) <br>  <br> **Stage 2** [[Stupefied 2]] and [[Clumsy]] 2 (1 round) <br>  <br> **Stage 3** [[Stupefied 4]] and [[Clumsy]] 4 (1 round) <br>  <br> **Stage 4** [[Paralyzed]] as changes completely overtake the body (1 round) <br>  <br> **Stage 5** the victim permanently transforms into an animal, fungus, or plant in mind and body as a permanent curse, and the affliction ends"
  - name: "Reject Tools"
    desc: "A creature hit by the gongorinan's club must succeed at a DC 30 [[Will]] save or [[Release]] any manufactured items it's holding."
armorclass:
  - name: AC
    desc: "31; **Fort** +24, **Ref** +21, **Will** +20"
health:
  - name: HP
    desc: "205; **Immunities** controlled, fear effects; **Resistances** mental 10, physical 10 except cold iron"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +24 (`pf2:1`), **Damage** 2d6+9 bludgeoning plus [[Reject Tools]]"
  - name: "Melee strike"
    desc: "Pincer +23 (`pf2:1`) (magical, unholy), **Damage** 2d6 mental plus 2d10+9 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tentacle +23 (`pf2:1`) (agile, magical, reach 10 ft., unarmed, unholy), **Damage** 2d6+9 bludgeoning plus 2d6 mental"
  - name: "Melee strike"
    desc: "Stinger +23 (`pf2:1`) (magical, unholy), **Damage** 2d6+9 piercing plus [[Gongorinan Venom]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30, attack +22<br>**6th** [[Cursed Metamorphosis]], [[Petrify]]<br>**4th** [[Unfettered Movement]] (Constant)<br>**3rd** [[One with Stone]] (At Will)"
abilities_bot:
  - name: "Disquieting Display"
    desc: "`pf2:2` The gongorinan opens its maw to reveal the forms [[Hidden]] there, making observers question their own bodies. Creatures in a @Template[emanation|distance:30] must attempt a DC 30 [[Will]] save, after which they are temporarily immune to further Disquieting Displays for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Clumsy]] 1 for 1 round. <br> - **Failure** The creature is [[Clumsy]] 2 and [[Slowed]] 1 for 1 round. <br> - **Critical Failure** As failure, but for 1 minute."
  - name: "Painful Limbs"
    desc: "`pf2:2` The gongorinan makes up to four Strikes against different targets, each using a different limb. All four Strikes count toward its multiple attack penalty, but the penalty doesn't increase until after the gongorinan has made all the attacks."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

While most qlippoths focus on wiping mortals from existence, gongorinans follow the divergent plan of trapping mortals in forms incapable of understanding their actions and performing any sin meriting condemnation to the Outer Rifts. What may seem as a mercy to some is a matter of dire necessity to the gongorinans, who see killing sinful mortals as tantamount to helping their foes.

Long before the creatures known as demons came to be the dominant force in the Outer Rifts, qlippoth ruled the innumerable cracks of the Outer Sphere. These inimical creatures are a form of primordial and alien evil that predates mortal life, and most immortal life as well. Since the rise of mortal sin and the associated expansion of demonic life through the Outer Rifts, qlippoth have been driven to their deepest reaches, and they seethe with rancor at the loss of their realms. Yet, rather than directly oppose demons, qlippoth instead turn to the source—mortal sin—and wage an endless war to eradicate all creatures capable of sinful acts so that the demonic tide might be turned back. To ensure they do not bolster their foe's ranks, they enact horrific transformations on their targets, converting their victims into beings incapable of discerning right from wrong; this renders them unable to be judged by Pharasma's courts and thus incapable of becoming fiends. Most mortals consider the ministrations of a qlippoth to be far worse than any fate awaiting them in the afterlife.

```statblock
creature: "Gongorinan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
