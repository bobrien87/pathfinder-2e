---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Norn"
level: "20"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+41; [[Greater Darkvision]], [[Lifesense]] (precise) 120 feet, [[Truesight]] (precise) 60 feet"
languages: "Common, Fey, Jotun (Truespeech)"
skills:
  - name: Skills
    desc: "Crafting +36, Deception +35, Intimidation +37, Medicine +38, Occultism +34, Performance +31, Religion +34, Lore (All) +28"
abilityMods: ["+7", "+6", "+6", "+6", "+10", "+7"]
abilities_top:
  - name: "Sense Fate"
    desc: "A norn automatically rolls a 20 when she rolls initiative."
  - name: "Triumvirate"
    desc: "This functions as the [[Coven]] ability, except only norns can join a triumvirate, and it functions only as long as exactly three norns are part of the triumvirate. A triumvirate grants the following spells: [[Cataclysm]], [[Foresight]], [[Manifestation]](once per day), [[Pinpoint]], and [[Revival]]."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Fated"
    desc: "When a creature is subject to a fortune effect from a norn and a misfortune effect from any source other than a norn (or vice versa), the norn's effect automatically counteracts the other effect and then takes place normally, rather than the two effects canceling each other out. If both the fortune and misfortune effect are from a norn, then the two cancel each other out as normal. At the GM's discretion, powerful entities related to fate or luck, like Desna, Magdh, or Pharasma, can't have their effects negated by this ability."
  - name: "Sever Fate"
    desc: "When a norn deals void damage with a Strike, she regains 10 Hit Points. The target must succeed at a DC 39 [[Fortitude]] save or become [[Drained]] 1 ([[Drained]] 2 on a critical failure). <br>  <br> Further void damage dealt by the norn increases the drained condition value by 1 on a failed save (or by 2 on a critical failure), to a maximum of [[Drained]] 4."
armorclass:
  - name: AC
    desc: "46; **Fort** +34, **Ref** +30, **Will** +38"
health:
  - name: HP
    desc: "375; regeneration 20 (deactivated by cold iron); **Immunities** off guard, void; **Weaknesses** cold iron 20"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 20 (Deactivated by Cold Iron)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Shift Fate"
    desc: "`pf2:r` **Trigger** A creature within 120 feet attempts a saving throw <br>  <br> **Effect** The creature rolls the saving throw twice, and then the norn decides which result applies. If the norn chooses the lower roll, this is a misfortune effect; if she chooses the higher roll, it's a fortune effect; if they're the same, she decides which trait to apply."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Norn Shears +38 (`pf2:1`) (deadly 2d8, magical, reach 10 ft., versatile p), **Damage** 4d4+15 slashing plus 6d6 void plus [[Sever Fate]]"
  - name: "Melee strike"
    desc: "Hand Of Fate +38 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 4d10+15 void plus [[Sever Fate]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 42, attack +34<br>**10th** [[Freeze Time]]<br>**9th** [[Phantasmagoria]]<br>**8th** [[Hidden Mind]] (Constant), [[Migration]], [[Quandary]]<br>**7th** [[Execute]], [[Retrocognition]]<br>**6th** [[Spellwrack]], [[Truesight]] (Constant)<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Read Omens]]<br>**2nd** [[Dispel Magic]]<br>**1st** [[Detect Magic]] (Constant)"
  - name: "Triumvirate Spells"
    desc: "DC 42, attack +34<br>**10th** [[Cataclysm]], [[Manifestation]], [[Revival]]<br>**9th** [[Foresight]]<br>**8th** [[Pinpoint]]<br>**6th** [[Cursed Metamorphosis]]<br>**5th** [[Illusory Scene]], [[Scouting Eye]]<br>**4th** [[Clairvoyance]], [[Talking Corpse]]<br>**3rd** [[Clairaudience]], [[Dream Message]]<br>**2nd** [[Augury]]<br>**1st** [[Charm]], [[Illusory Disguise]]"
abilities_bot:
  - name: "Snip Thread"
    desc: "`pf2:2` **Frequency** three times per day <br>  <br> **Effect** The norn produces a golden thread linked to the fate of a creature within 100 feet of her, then snips it short with her shears. The target takes 100 void damage (DC 42 [[Fortitude]] save). If the target is reduced to 0 Hit Points from this damage, the thread is completely severed and the creature dies immediately. <br>  <br> A creature slain by Snip Thread can't be restored to life except by a [[Wish]] ritual or similarly powerful magic; or by divine intervention. Regardless of the outcome of their saving throw, a creature targeted by Snip Thread then becomes temporarily immune for 24 hours. <br>  <br> The norn can't use Snip Thread again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Ancient beyond imagining, norns are powerful fey women who hold in their hands the physical manifestation of fate and destiny in the form of golden thread. They watch over all life, intervening with reluctance when called upon—or with a vengeance when the strands of fate are twisted and abused by lesser beings. They cut imposing figures, standing 14 feet tall and weighing 800 pounds.

Norns' relationship with the Eldest of the First World is complex. Many among norns serve Magdh the Three, the triune Eldest who some norns believe to be the first norn triumvirate bound together into one entity, as Magdh has three bodies: a Maiden, a Mother, and a Matriarch. Magdh claims to be watching the threads of fate for some ominous prophesied cataclysm, and in addition to assisting in her divinations, Magdh expects the norns who serve her to follow her cryptic commands to help nudge the future away from the brink. However, norns are powerful beings in their own right, themselves capable of granting divine power, and many balk at serving the enigmatic demigod. These norns find the other Eldest even more alien and challenging to interact with, for they believe that while the Eldest wield great power, even these powerful beings should not be granted leave to meddle with fate as much as they desire.

While even the weakest of the Eldest could destroy an unaffiliated norn with ease, they tend to obey the proclamations and judgments of norns when they are spoken. These norns, for their part, use their perceived neutrality judiciously. They know better than to issue too many demands to the Eldest, lest the capricious demigods grow frustrated. And so the balance of power remains tenuous between unaffiliated norns and the Eldest, as it has for eons. Norns know that it's merely a matter of time before the Eldest lose their respect for this tradition and start acting entirely as they please, despite norns' best efforts to rein in their most disruptive actions.

Followers of Fate
In the mortal Universe, some mortals worship norns as deities, while others, especially witches and bards, admire them as patrons or muses. Those who uphold norns as deities are known as Followers of Fate. Norns neither discourage this veneration nor go out of their way to support such worship. Clerics who venerate norns might worship a specific norn or norn triumvirate, or all norns as a whole, but they gain the same benefits regardless of their choice. The religious symbol of Followers of Fate is a pair of shears cutting a golden thread, and their areas of concern are destiny, fate, and the aging process.

```statblock
creature: "Norn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
