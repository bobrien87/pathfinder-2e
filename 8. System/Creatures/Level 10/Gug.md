---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gug"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]]"
languages: "Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +23, Stealth +19, Survival +17"
abilityMods: ["+7", "+3", "+6", "+0", "+3", "+0"]
abilities_top:
  - name: "Eerie Flexibility"
    desc: "Despite its size, the gug's multiple joints allow it to fit through tight spaces as if it were a Medium creature. While [[Squeezing]], it can move at its full Speed."
armorclass:
  - name: AC
    desc: "30; **Fort** +22, **Ref** +17, **Will** +19"
health:
  - name: HP
    desc: "175"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +23 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 2d12+13 piercing"
  - name: "Melee strike"
    desc: "Claw +23 (`pf2:1`) (agile, reach 15 ft., unarmed), **Damage** 2d8+13 slashing"
spellcasting: []
abilities_bot:
  - name: "Furious Claws"
    desc: "`pf2:2` The gug makes up to four claw Strikes, each against a different target. These attacks all count toward the gug's multiple attack penalty, but the penalty doesn't increase until after the gug makes all its attacks."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A gug's most horrid feature is its barrel-shaped head, which splits vertically to reveal numerous rows of sharp, yellow teeth and an open throat. Its eyes on either side of its head-jaw are small but keen. Bony ridges protect its eyes from the frantic flailing of its prey, as it prefers meals of raw and writhing meat over fungi and molds. It grips said prey with powerful arms that split at the elbow into a pair of forearms, giving it four clawed paws. These monstrous brutes are covered with shaggy black fur, often crusted with blood and gore.

Although gugs may seem bestial, they have keen and wicked intellects. Gugs lair far underground, but they sometimes come to the surface to hunt during dark nights, either alone or in small groups. As they possess voracious appetites, most gugs consume the creatures they catch, but some instead kidnap their victims and retreat below the surface, leaving only a lingering stench and odd, clawed paw-prints. Victims are taken to rancid lairs marked with strange runes and sacrificed to the gugs' wicked gods of blood, darkness, and nightmares. Dire rumors tell of lightless gug cities made of titanic blocks of stone far underground, where powerful gug leaders preach their vile doctrines to mobs of howling gugs.

Gugs have a strange relationship with ghouls, which seems to date from their shared origin in a distant subterranean world. Gugs live in fear of ghouls, despite towering over them; however, this strange fear doesn't apply to ghasts, whom gugs consume as voraciously as they do other creatures.

Gugs stand 16 feet tall and weigh 2,000 pounds, although they have an eerie, graceful gait that belies their immense size. Their light step and ability to squeeze through very small crannies makes gugs common bogeymen in tales of strange disappearances or bloody massacres.

Some particularly bloodthirsty gugs gain awful powers as gifts from their eldritch patrons. These monsters are known as savants, are never less than 12th level in power, and gain several occult innate spells. Though each savant's precise mix of spells varies, normally, these spells grant invisibility, offer power to manipulate and change rock, or invoke awful and destructive energies upon living flesh.

```statblock
creature: "Gug"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
