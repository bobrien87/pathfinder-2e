---
type: creature
group: ["Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Festrog"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +6, Stealth +7, Survival +5"
abilityMods: ["+4", "+2", "+2", "+0", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15 void healing; **Fort** +7, **Ref** +7, **Will** +6"
health:
  - name: HP
    desc: "25; **Immunities** bleed, death effects, disease, paralyzed, poison, sleep, unconscious"
abilities_mid:
  - name: "Diseased Pustules"
    desc: "Whenever the festrog takes piercing or slashing damage, creatures adjacent to the festrog take 1d4 poison damage (DC 14 [[Reflex]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (unarmed), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Claw +9 (`pf2:1`) (agile, unarmed), **Damage** 1d4+4 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Feast"
    desc: "`pf2:1` **Requirements** The festrog's last action was a jaws Strike that damaged a living creature <br>  <br> **Effect** The festrog tears into the creature's flesh and gulps it down voraciously, dealing 1d4 slashing damage to the creature and gaining temporary Hit Points equal to the damage dealt. These temporary HP last for 1 minute."
  - name: "On All Fours"
    desc: "`pf2:1` **Requirements** The festrog has nothing in their hands <br>  <br> **Effect** The festrog Strides with a +10-foot circumstance bonus to their Speed."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Spawned from corpses of those who died of illness or starvation and were twisted by void energy, festrogs display a viciousness that rivals other undead. They resemble decaying humanoids, but with elongated arms, teeth, and bone-like spikes protruding from their upper backs. Festrogs' tendency to run on all fours has led to them gaining the moniker dog-ghouls, causing the unwary to mistake them for mindless predators.

Festrogs are in fact intelligent, stalking victims in packs and choosing hunting grounds that suit their abilities. They can often be found roaming farmlands, open forests, or wide plains, anywhere they can use their quadrupedal speed to overtake quarry. Belying their mindless appearance, festrogs use tactics similar to those of hunters with hounds: the leader of the pack often flushes prey from cover so that the victim can be brought down by the pack.

Researchers of the necromantic processes that create risen corpses have found that festrogs spawn more often from slow demises than sudden deaths. Festrogs typically animate from corpses afflicted with disease, while victims of violence are more likely to become more common undead, such as zombies. One well-documented way to create a festrog is to have scavengers feed on the dead flesh before animating it. This potentially explains why festrogs most often arise in remote areas stricken with famine and desperate predators.

Though most festrogs arise from humans and other prevalent humanoids, other creatures that die in the same circumstances can rise as festrogs. Festrogs that were once larger humanoids, such as ogres, hill giants, or trolls behave similarly to other humanoid festrogs and are simply larger and more powerful. More peculiar are the beastkin festrogs formed of quadrupedal animals, which typically have feet or hooves instead of hands, travel on all fours at all times, and have only animal intelligence. In fact, some humanoid festrogs capture and starve beastkin in hopes of the creatures rising as grotesque festrog pets.

```statblock
creature: "Festrog"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
